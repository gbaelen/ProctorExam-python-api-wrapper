class Exam():
    def __init__(self, data, connector=None):
        self.id = data["id"]
        self.institute_id = data["institute_id"]
        self.name = data["name"]
        self.terms = data["terms"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.duration_minutes = data["duration_minutes"]
        self.clipboard = data["clipboard"]
        self.start_time = data["start_time"]
        self.mode = data["mode"]
        self.upload_answers = data["upload_answers"]
        self.token = data["token"]
        self.user_id = data["user_id"]
        self.end_time = data["end_time"]
        self.restrictions = data["restrictions"]
        self.published = data["published"]
        self.status = data["status"]
        self.for_reviewing = data["for_reviewing"]
        self.uploaded_exam_documents_file_name = data["uploaded_exam_documents_file_name"]
        self.uploaded_exam_documents_content_type = data["uploaded_exam_documents_content_type"]
        self.uploaded_exam_documents_file_size = data["uploaded_exam_documents_file_size"]
        self.uploaded_exam_documents_updated_at = data["uploaded_exam_documents_updated_at"]
        self.timezone = data["timezone"]
        self.use_duration = data["use_duration"]
        self.global_proctoring = data["global_proctoring"]
        self.global_reviewing = data["global_reviewing"]
        self.exam_language = data["exam_language"]
        self.archived = data["archived"]
        self.web_cam = data["web_cam"]
        self.mobile_cam = data["mobile_cam"]
        self.screen_share = data["screen_share"]
        self.live_proctoring = data["live_proctoring"]
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
