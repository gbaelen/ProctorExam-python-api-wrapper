class Exam():
    def __init__(self, id=None, institute_id=None, name="", terms=None, created_at=None, updated_at=None, duration_minutes=None, clipboard=None, start_time=None, mode=None, upload_answers=None, token=None, user_id=None, end_time=None, restrictions=None, published=None, status=None, for_reviewing=None, uploaded_exam_documents_file_name=None, uploaded_exam_documents_content_type=None, uploaded_exam_documents_file_size=None, uploaded_exam_documents_updated_at=None, timezone=None, use_duration=None, global_reviewing=None, global_proctoring=None, exam_language=None, archived=None, web_cam=None, mobile_cam=None, screen_share=None, live_proctoring=None):
        self.id = id
        self.institute_id = institute_id
        self.name = name
        self.terms = terms
        self.created_at = created_at
        self.updated_at = updated_at
        self.duration_minutes = duration_minutes
        self.clipboard = clipboard
        self.start_time = start_time
        self.mode = mode
        self.upload_answers = upload_answers
        self.token = token
        self.user_id = user_id
        self.end_time = end_time
        self.restrictions = restrictions
        self.published = published
        self.status = status
        self.for_reviewing = for_reviewing
        self.uploaded_exam_documents_file_name = uploaded_exam_documents_file_name
        self.uploaded_exam_documents_content_type = uploaded_exam_documents_content_type
        self.uploaded_exam_documents_file_size = uploaded_exam_documents_file_size
        self.uploaded_exam_documents_updated_at = uploaded_exam_documents_updated_at
        self.timezone = timezone
        self.use_duration = use_duration
        self.global_proctoring = global_proctoring
        self.global_reviewing = global_reviewing
        self.exam_language = exam_language
        self.archived = archived
        self.web_cam = web_cam
        self.mobile_cam = mobile_cam
        self.screen_share = screen_share
        self.live_proctoring = live_proctoring

    @staticmethod
    def generate_exam_from_response(data):
        return Exam(**data)

    def get_exam_type(self):
        if self.mode[4] is "1":
            return "Live Proctoring"
        elif self.mode[3] is "1":
            return "Record&Review"
        else:
            return "Classroom"

class ExamList():
    def __init__(self):
        self.__id = 0
        self.__exams = []

    def __iter__(self):
        self.__id = 0
        return self

    def __next__(self):
        if self.__id < len(self.__exams):
            exam = self.__exams[self.__id]
            self.__id += 1
            return exam
        else:
            raise StopIteration

    def add(self, exam):
        self.__exams.append(exam)

    def size(self):
        return len(self.__exams)
