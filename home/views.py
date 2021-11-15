from django.shortcuts import *
from django.http import *
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from django.db.utils import IntegrityError
from .models import *
from django.db.models import *

from judge.models import *

def get_role_and_col(ratings):
	__leveling = [x for x in range(1200, 2801, 200)]
	__color = ['grey', 'green', 'teal', 'blue', 'purple', 'violet', 'olive', 'yellow', 'orange', 'red']
	res = ['Level 10', 'red']
	for i in range(len(__leveling)):
		if ratings <= __leveling[i]:
			res = [f'Level {i+1}', __color[i]]
			break
	return res

def about_page(req):
	return render(req, 'pages/about.html', {
		#'exLevelColor': [[level[i]-1, color[i]]]
	})

def index(req):
	prof = Profile.objects.all()
	for p in prof:
		p.level = get_role_and_col(p.ratings)[0]
		p.color = get_role_and_col(p.ratings)[1]
		p.save()
	prob = Problem.objects.all().order_by('-publish_date')[:20]
	blog = Blog.objects.all().order_by('-publish_date')[:20]
	for k, v in enumerate(blog):
		if len(v.title + ' - ' + v.author.user.username) > 40:
			blog[k].title = v.title[:22] + '...'
	display_blog = Blog.objects.filter(on_feed=True).order_by('-publish_date')[:10]
	a = display_blog[0]
	a.viewed += 1
	a.save()
	return render(req, 'pages/index.html', {'newest_prob': prob, 'newest_blog': blog, 'feed_blog': display_blog})

def register_page(req):
	if req.method == "POST":
		username = req.POST["usr_name"]
		if not User.objects.filter(username__iexact=username).exists():
			email = req.POST["usr_email"]
			passwd = req.POST["usr_passwd"]
			repasswd = req.POST["usr_re_passwd"]
			if len(req.POST["usr_passwd"]) < 8 and len(req.POST["usr_passwd"]) > 25:
				return render(req, 'pages/register.html', {'msg_err': 'Your password must be at least 8 - 25 characters.'})
			elif passwd == repasswd:
				try:
					for i in username:
						if len(username) < 3 or len(username) > 30 or i not in '0123456789abcdefghijklmnopqrstuvwxyzABCDEFHGHIJKLMNOPQRSTUVWXYZ':
							return render(req, 'pages/register.html', {'msg_err': 'Your username must be at least 4 - 30 characters and must not have any special characters.'})
					user = User.objects.create_user(username, email, passwd)
					Profile.objects.create(user=user, ratings=0.0)
					user.save()
				except IntegrityError:
					return render(req, 'pages/register.html', {'msg_err': 'Username is alreay exists.'})
				return render(req, 'pages/registered.html')
			else:
				return render(req, 'pages/register.html', {'msg_err': 'Your password doesn\'t match.'})
		else:
			return render(req, 'pages/register.html', {'msg_err': 'Username is alreay exists.'})
	if req.method == "GET":
		return render(req, 'pages/register.html')

def login_page(req):
	if req.method == "POST":
		username = req.POST["usr_name"]
		password = passwd = req.POST["usr_passwd"]
		user = authenticate(req, username=username, password=password)
		if user is not None:
			login(req, user)
			return redirect('/')
		else:
			return render(req, 'pages/login.html', {'msg_err': 'Please check your username or password and try again.'})
	elif req.method == "GET":
		if req.user.is_authenticated:
			logout(req)
		return render(req, 'pages/login.html')

def logout_page(req):
	if req.user.is_authenticated:
		logout(req)
	return redirect('/')

def profile_page(req, qry_user=None):
	if (req.user.is_authenticated and qry_user is None) or ((qry_user is not None) and len(User.objects.filter(username=qry_user)) != 0):
		u = User.objects.filter(username=qry_user or req.user.username)[0]
		prof = Profile.objects.filter(user=u)[0]
		prof_rc = get_role_and_col(prof.ratings)
		prof.level = prof_rc[0]
		prof.color = prof_rc[1]
		prof.save()
		user_problem = Problem.objects.filter(author=prof).order_by('-publish_date')
		user_blog = Blog.objects.filter(author=prof).order_by('-publish_date')
		for k, v in enumerate(user_blog):
			if len(v.title) > 33:
				user_blog[k].title = v.title[:30] + '...'
		return render(req, 'pages/profile.html', {
			'prof_firstname': u.first_name,
			'prof_lastname': u.last_name,
			'prof_slogan': prof.slogan,
			'prof_facebook': prof.social_facebook,
			'prof_github': prof.social_github,
			'prof_ratings': prof.ratings,
			'prof_role': prof_rc[0],
			'prof_color': prof_rc[1],
			'prof_user': qry_user or req.user.username,
			'prof_solved': prof.total_problems,
			'prof_ratio': prof.total_ratio,
			'prof_match': prof.total_match,
			'prof_win': prof.total_win,
			'prof_diff': str(prof.total_diff),
			'user_problem': user_problem,
			'user_blog': user_blog
		})
	else:
		raise Http404

def profile_settings_page(req):
	if req.method == "GET":
		if req.user.is_authenticated:
			u = User.objects.filter(username=req.user.username)[0]
			prof = Profile.objects.filter(user=u)[0]
			return render(req, 'pages/profile_settings.html', {
				'ulastname': u.last_name,
				'ufirstname': u.first_name,
				'pslogan': prof.slogan,
				'pfacebook': prof.social_facebook,
				'pgithub': prof.social_github,
			})
	elif req.method == "POST":
		if req.user.is_authenticated:
			u = User.objects.filter(username=req.user.username)[0]
			p = Profile.objects.filter(user=u)[0]
			u.first_name = req.POST['firstname']
			u.last_name = req.POST['lastname']
			u.save()
			p.slogan = req.POST['slogan']
			p.social_facebook = req.POST['social-facebook']
			p.social_github = req.POST['social-github']
			p.save()
			return redirect('/profile/')
	raise Http404

def ranking_page(req):
	qry = {
		'rev-rating': 'ratings',
		'rating': '-ratings',
	}
	ranking_list = Profile.objects.all()
	if 'search-user' in req.POST:
		ranking_list = ranking_list.filter(user__username__icontains=req.POST['search-user'])
	ranking_list = ranking_list.order_by('-ratings')
	if 'filter-tags' in req.POST:
		ranking_list = Profile.objects.order_by(qry[req.POST['filter-tags']])
	return render(req, 'pages/ranking.html', {'ranking_list': ranking_list})

def problemset_page(req):
	match req.method:
		case "GET":
			problems_list = Problem.objects.order_by("-publish_date")
			return render(req, 'pages/problem/problemset.html', {'problems_list': problems_list, 'latest_problems': problems_list[:30]})
	raise Http404

def detail_problem(req, prob_id):
	problem = Problem.objects.filter(problem_id=prob_id)[0]
	sample_in = problem.sample_input.replace('\r', '').split('\n\n')
	sample_out = problem.sample_output.replace('\r', '').split('\n\n')
	sample = [[sample_in[x], sample_out[x]] for x in range(len(sample_in))]
	submission = False
	statcol = {
		'AC': ['green', 'checkmark'],
		'WA': ['red', 'times'],
		'TLE': ['orange', 'clock'],
		'RTE': ['orange', 'bug'],
		'CE': ['orange', 'server'],
	}
	if req.user.is_authenticated:
		submission = Submission.objects.filter(author__user=req.user, problem=problem).order_by('-publish_date')
	return render(req, 'pages/problem/problem_detail.html', {'problem': problem, 'sample': sample, 'submission': submission, 'statcol': statcol})

def create_blog_page(req):
	if req.user.is_authenticated:
		if req.method == 'POST':
			entry_id = hashlib.sha1(bytes(req.POST['blog_title'] + '`'.join(req.user.username), encoding='utf-8')).hexdigest()
			blog = Blog.objects.create(entry_id=entry_id, author=Profile.objects.filter(user=req.user)[0], title=req.POST['blog_title'], content=req.POST['blog_content'])
			blog.save()
			return redirect(f'/blog/entry/{entry_id}/')
		else:
			return render(req, 'pages/blog/cr_blog.html', {'all_prof': Profile.objects.filter(~Q(user=req.user))})
	raise Http404

def blog_entry_page(req, blog_entry):
	if blog_entry == None:
		raise Http404
	blog = Blog.objects.filter(entry_id=blog_entry)[0]
	comment = Comment.objects.filter(blog=blog).order_by('-publish_date')
	blog.viewed += 1
	blog.save()
	return render(req, 'pages/blog/blog_entry.html', {
		'bentry': blog_entry,
		'btitle': blog.title,
		'bcontent': blog.content,
		'bviewer': blog.viewed,
		'bpublish': blog.publish_date,
		'bnewfeed': blog.on_feed,
		'bauthor': (blog.author, blog.author.color),
		'bcomment': comment,
	})

def blog_edit_page(req, blog_entry):
	if blog_entry != None:
		blog = Blog.objects.filter(entry_id=blog_entry)[0]
		if req.method == "GET":
			if req.user.is_authenticated and req.user.username == blog.author.user.username:
				return render(req, 'pages/blog/blog_edit.html', {'blog': blog})
		elif req.method == "POST":
			if req.user.is_authenticated and req.user.username == blog.author.user.username:
				blog.title = req.POST['blog_title']
				blog.content = req.POST['blog_content']
				blog.save()
				return redirect(f'/blog/entry/{blog_entry}/')
	raise Http404

def blog_page(req):
	qry = {
		'alphabetical': 'title',
		'-alphabetical': '-title',
		'latest_date': '-publish_date',
		'oldest_date': 'publish_date',
		'most_view': '-viewed',
		'least_view': 'viewed',
	}
	filter_tags = req.POST.getlist('filter-tags')
	fr, to = 1, 50
	blog = Blog.objects.all().order_by('-publish_date')
	for i in filter_tags:
		blog = blog.order_by(qry[i])

	return render(req, 'pages/blog/blog_page.html', {'blog_list': blog})

def blog_delete_page(req, blog_entry):
	try:
		blog = Blog.objects.filter(entry_id=blog_entry)[0]
	except:
		raise Http404
	if req.user.is_authenticated and req.user.username == blog.author.user.username:
		if req.method == "GET":
			return render(req, 'pages/blog/blog_delete.html', {'entry': blog_entry})
		elif req.method == "POST":
			if req.POST['retype-title'] == blog.title:
				blog.delete()
				return redirect('/blog/')
			else:
				return render(req, 'pages/blog/blog_delete.html', {'entry': blog_entry, 'msg_err': 'Your re-type blog title doesn\'t match. We can\'t delete this blog for you. Please try again.'})
	raise Http404

def blog_nfauthorize_page(req, blog_entry):
	try:
		blog = Blog.objects.filter(entry_id=blog_entry)[0]
	except:
		raise Http404
	if req.user.is_authenticated:
		if req.user.is_superuser or req.user.is_staff or req.user.groups.filter(name="Blog Moderator").exists():
			blog.on_feed = True
			blog.save()
			return redirect(f'/blog/entry/{blog_entry}/')
	raise Http404

def blog_comment_page(req, blog_entry):
	try:
		blog = Blog.objects.filter(entry_id=blog_entry)[0]
	except:
		raise Http404
	if req.user.is_authenticated and req.POST['cmt_content']:
		p = Profile.objects.filter(user=req.user)[0]
		cmt = Comment.objects.create(blog=blog, author=p, comment_description=req.POST['cmt_content'])
		cmt.save()
		result = {'content': cmt.comment_description, 'author': p}
		return JsonResponse(result)
	raise Http404

def delete_comment_page(req, blog_entry, cmt_id):
	if blog_entry and cmt_id:
		if req.user.is_authenticated:
			if req.user.is_superuser or req.user.is_staff or req.user.groups.filter(name="Blog Moderator").exists():
				cmt = Comment.objects.filter(comment_id=cmt_id)[0]
				cmt.delete()
				return redirect(f'/blog/entry/{blog_entry}/')
	raise Http404
