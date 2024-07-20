import graphene
from graphene_django.types import DjangoObjectType
from .models import *

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class MainPageType(graphene.ObjectType):
    category = graphene.Field(CategoryType)
    post_list = graphene.List(PostType)


class ListOfCategoryContent(graphene.ObjectType):
    ListOfPost = graphene.List(MainPageType)


class Query(graphene.ObjectType):
    all_Category = graphene.List(CategoryType)
    all_Post = graphene.List(PostType)
    list_of_category_content = graphene.Field(ListOfCategoryContent, categorydata=graphene.String())

    def resolve_all_Category(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_Post(self, info, **kwargs):
        return Post.objects.all()

    def resolve_list_of_category_content(self, info,categorydata ):
        categories = Category.objects.all()
        if categorydata:
            categories = Category.objects.filter(name=categorydata).order_by('-id')[:4]

        listOfmainPageContent = []
        for category in categories:
            pageData = Post.objects.filter(category=category)
            spliterByCategory = MainPageType(
                category = category,
                post_list = pageData
            )
            listOfmainPageContent.append(spliterByCategory)
        return (ListOfCategoryContent(ListOfPost=listOfmainPageContent))



#  page_info = PageInfoType(
#             total_items=paginator.count,
#             has_next_page=paginated_data.has_next(),
#             has_previous_page=paginated_data.has_previous(),
#             total_pages=paginator.num_pages,
#         )






schema = graphene.Schema(query=Query)
