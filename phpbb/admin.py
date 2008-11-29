from django.contrib import admin
from django.contrib.phpbb.models import ForumForum
from django.contrib.phpbb.models import ForumPost
from django.contrib.phpbb.models import ForumTopic
from django.contrib.phpbb.models import ForumUser

class ForumForumAdmin(admin.ModelAdmin):
    list_display = (
            'forum_name',
            'forum_id',
            'forum_desc',
            )
admin.site.register(ForumForum, ForumForumAdmin)
class ForumTopicAdmin(admin.ModelAdmin):
    list_display = (
        'topic_title',
        'topic_id',
        'topic_time',
    )
admin.site.register(ForumTopic, ForumTopicAdmin)
class ForumPostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'get_absolute_url', 'post_time', )
admin.site.register(ForumPost, ForumPostAdmin)
class ForumUserAdmin(admin.ModelAdmin):
    list_display = ('username',
                    'user_id',
                    'user_regdate',
                    'user_posts',
                    'user_email', )
admin.site.register(ForumUser, ForumUserAdmin)
