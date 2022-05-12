from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note


class NoteListCreateAPIView(APIView):
    def get(self, request):
        notes = Note.objects.all()

        res = []
        for note in notes:
            res.append({
                'title': note.title,
                'message': note.message,
                'public': note.public,
                'create_at': note.create_at,
                'update_at' : note.update_at,
            })

        return Response(res)


    # def post(self, request: Request):
    #     data = request.data
    #     note = Note(**data)
    #
    #     note.save(force_insert=True)
    #
    #     return Response(
    #         serializers.note_created(note),
    #         status=status.HTTP_201_CREATED
    #     )