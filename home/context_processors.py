from .models import Profile
from django.contrib.auth.models import User

def role_ratings(req):
	if req.user.is_authenticated:
		ratings = Profile.objects.filter(user=req.user).values_list('ratings')[0][0]
		__leveling = [x for x in range(1200, 2801, 200)]
		__color = ['grey', 'green', 'teal', 'blue', 'purple', 'violet', 'olive', 'yellow', 'orange', 'red']
		res = ['Level 10', 'red']
		for i in range(len(__leveling)):
			if ratings <= __leveling[i]:
				res = [f'Level {i+1}', __color[i]]
				break
		return {'role_ratings_role': res[0], 'role_ratings_color': res[1], 'user_ratings': ratings}
	return {}