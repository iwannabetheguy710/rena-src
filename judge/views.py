from django.shortcuts import *
from django.http import *
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from .models import *

import hashlib, os, subprocess, codecs, time

def judge(req, code, lang, problem_id, hashfile):
	problem = Problem.objects.filter(problem_id=problem_id)[0]
	testcase = Testcase.objects.filter(problem=problem)[0]
	testcase.inp = testcase.inp.split('\r\n\r\n')
	testcase.out = testcase.out.split('\r\n\r\n')
	user_profile = Profile.objects.filter(user=req.user)[0]
	fileex = {
		'text/x-c++src': 'cpp',
		'text/x-python': 'py',
		'text/x-ruby': 'rb',
		'text/x-csharp': 'cs',
		'text/x-pascal': 'pas',
	}
	compiler = {
		'text/x-c++src': 'g++ ./tmp/{0}.cpp -o ./tmp/{0} -std=c++17 -O2',
		'text/x-pascal': 'fpc ./tmp/{0}.pas -o./tmp/{0} -O2'
	}
	runner = {
		'text/x-c++src': './tmp/{0}',
		'text/x-pascal': './tmp/{0}',
		'text/x-python': 'python ./tmp/{0}.py',
		'text/x-ruby': 'ruby ./tmp/{0}.rb',
	}
	submitfile = codecs.open(f"./tmp/{hashfile}.{fileex[lang]}", 'w', encoding='utf-8')
	submitfile.write(code.replace('\r', ''))
	submitfile.close()
	for i, v in enumerate(testcase.inp):
		inpfile = codecs.open(f'./tmp/{hashfile}_{i}.inp', 'w', encoding='utf-8')
		inpfile.write(v)
		inpfile.close()
	status = 'AC: Accepted'
	if lang in compiler:
		start = time.process_time()
		c = subprocess.run(compiler[lang].format(hashfile))
		end = time.process_time()
		if c.returncode != 0:
			status = "CE: Compilation Error".split(': ')
			submission = Submission.objects.filter(submit_id=hashfile, author=user_profile, problem=problem).order_by('-publish_date')[0]
			submission.status_code = status[0]
			submission.message = status[1]
			submission.runtime = 0
			submission.save()
			status.append(submission.runtime)
			return status
	start, end = 0, 0
	for i, v in enumerate(testcase.out):
		fi = codecs.open(f'./tmp/{hashfile}_{i}.inp', 'r', encoding='utf-8')
		try:
			start = time.process_time()
			process = subprocess.run(runner[lang].format(hashfile), stdin=fi, stdout=subprocess.PIPE, timeout=float(problem.time_limit) + 0.010)
			end = time.process_time()
			if process.returncode != 0:
				status = "RTE: Runtime error"
				break
		except subprocess.TimeoutExpired:
			start, end = 0, 9.999
			status = f'TLE: Time limit exeeded'
			break
		o = process.stdout.decode('utf-8')
		o = o.split('\r\n')
		while len(o) and o[-1] == '':
			o = o[:-1]
		for j, line in enumerate(o):
			while len(o[j][-1]) and o[j][-1] == ' ':
				o[j] = o[j][:-1]
		o = '\r\n'.join(o)
		if o != v:
			status = f'WA: Wrong answer'
			break
	status = status.split(': ')
	if status[0] == 'AC':
		if not Submission.objects.filter(author=user_profile, status_code='AC', problem=problem).exists():
			user_profile.total_problems += 1
			user_profile.save()
			problem.accepted_user += 1
			problem.save()
	submission = Submission.objects.filter(submit_id=hashfile, author=user_profile, problem=problem).order_by('-publish_date')[0]
	submission.status_code = status[0]
	submission.message = status[1]
	submission.runtime = int((end - start) * 1000)
	submission.save()
	status.append(submission.runtime)
	return status

@csrf_exempt
def submission_judge_page(req, problem_id):
	if req.method == "POST":
		if req.user.is_authenticated:
			status = judge(req, req.POST['code_content'], req.POST['lang_select'], problem_id, req.POST['hashfile'])
			result = {
				'statuscode': status[0],
				'statusmsg': status[1],
				'statusruntime': status[2],
			}
			return JsonResponse(result)
	raise Http404

def submission_page(req, problem_id):
	if req.user.is_authenticated:
		problem = Problem.objects.filter(problem_id=problem_id)[0]
		profile = Profile.objects.filter(user=req.user)[0]
		statcol = {
			'AC': ['green', 'checkmark'],
			'WA': ['red', 'times'],
			'TLE': ['orange', 'clock'],
			'RTE': ['orange', 'bug'],
			'CE': ['orange', 'server'],
		}
		language = {
			'text/x-c++src': 'C++',
			'text/x-python': 'Python',
			'text/x-ruby': 'Ruby',
			'text/x-csharp': 'C#',
			'text/x-pascal': 'Pascal',
		}
		hashfile = hashlib.sha1(bytes(req.POST['code-content'] + str(req.user), encoding='utf-8')).hexdigest()
		#status = judge(req, req.POST['code-content'], req.POST['lang-select'], problem_id, hashfile)
		try:
			nxt_sub = Submission.objects.create(submit_id=hashfile, author=profile, problem=problem, language=language[req.POST['lang-select']])
			nxt_sub.save()
		except:
			pass
		submission = Submission.objects.filter(author=profile, problem=problem).order_by('-publish_date')
		return render(req, 'pages/problem/problem_submission.html', {
			'problem': problem,
			'profile': profile,
			'submission': submission,
			'statcol': statcol,
			'code_content': req.POST['code-content'],
			'lang_select': req.POST['lang-select'],
			'hashfile': hashfile,
		})
	raise Http404