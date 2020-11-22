class Exam():
    def __init__(self, data, connector=None):
        self.id = data["id"] if "id" in data else None
        self.institute_id = data["institute_id"] if "institute_id" in data else None
        self.name = data["name"] if "name" in data else None
        self.terms = data["terms"] if "terms" in data else None
        self.created_at = data["created_at"] if "created_at" in data else None
        self.updated_at = data["updated_at"] if "updated_at" in data else None
        self.duration_minutes = data["duration_minutes"] if "duration_minutes" in data else None
        self.clipboard = data["clipboard"] if "clipboard" in data else None
        self.start_time = data["start_time"] if "start_time" in data else None
        self.mode = data["mode"] if "mode" in data else None
        self.upload_answers = data["upload_answers"] if "upload_answers" in data else None
        self.token = data["token"] if "token" in data else None
        self.user_id = data["user_id"] if "user_id" in data else None
        self.end_time = data["end_time"] if "end_time" in data else None
        self.restrictions = data["restrictions"] if "restrictions" in data else None
        self.published = data["published"] if "published" in data else None
        self.status = data["status"] if "status" in data else None
        self.for_reviewing = data["for_reviewing"] if "for_reviewing" in data else None
        self.uploaded_exam_documents_file_name = data["uploaded_exam_documents_file_name"] if "uploaded_exam_documents_file_name" in data else None
        self.uploaded_exam_documents_content_type = data["uploaded_exam_documents_content_type"] if "uploaded_exam_documents_content_type" in data else None
        self.uploaded_exam_documents_file_size = data["uploaded_exam_documents_file_size"] if "uploaded_exam_documents_file_size" in data else None
        self.uploaded_exam_documents_updated_at = data["uploaded_exam_documents_updated_at"] if "uploaded_exam_documents_updated_at" in data else None
        self.timezone = data["timezone"] if "timezone" in data else None
        self.use_duration = data["use_duration"] if "use_duration" in data else None
        self.global_proctoring = data["global_proctoring"] if "global_proctoring" in data else None
        self.global_reviewing = data["global_reviewing"] if "global_reviewing" in data else None
        self.exam_language = data["exam_language"] if "exam_language" in data else None
        self.archived = data["archived"] if "archived" in data else None
        self.web_cam = data["web_cam"] if "web_cam" in data else None
        self.mobile_cam = data["mobile_cam"] if "mobile_cam" in data else None
        self.screen_share = data["screen_share"] if "screen_share" in data else None
        self.live_proctoring = data["live_proctoring"] if "live_proctoring" in data else None
        self.connector = connector

    @staticmethod
    def generate_exam_from_response(data, connector=None):
        return Exam(data, connector=connector)

    def get_exam_type(self):
        if self.mode[4] is "1":
            return "Live Proctoring"
        elif self.mode[3] is "1":
            return "Record&Review"
        else:
            return "Classroom"

    def is_mobile_on(self):
        #TODO: Confirm 3 is the mobile
        if self.mode[3] is "1":
            return True

        return False

    def update(self):
        """
        Potentially: Will call the connector to update the exam and get the created exam to replace update values here and diplay them
        """
        pass

    def delete(self):
        pass

    def get_students(self):
        pass

    def search_student_by_email(self):
        pass

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

    def __getitem__(self, key):
        return self.__exams[key]

    def add(self, exam):
        self.__exams.append(exam)

    def remove_at(self, id):
        self.__exams.pop(id)

    def size(self):
        return len(self.__exams)

    def find_student():
        pass
