class Student():
    def __init__(self, data, connector=None):
        self.id=data["id"]
        self.session_id=data["session_id"]
        self.student_id=data["student_id"]
        self.time_slot=data["time_slot"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]
        self.email=data["email"]
        self.pin_code=data["pin_code"]
        self.operating_system=data["operating_system"]
        self.browser=data["browser"]
        self.browser_version=data["browser_version"]
        self.status=data["status"]
        self.token=data["token"]
        self.screenshare_check=data["screenshare_check"]
        self.microphone_check=data["microphone_check"]
        self.speakers_check=data["speakers_check"]
        self.webcam_check=data["webcam_check"]
        self.mobile_check=data["mobile_check"]
        self.dummy_exam_survey=data["dummy_exam_survey"]
        self.skip_requirements=data["skip_requirements"]
        self.send_confirmation=data["send_confirmation"]
        self.name=data["name"]
        self.start_time=data["start_time"]
        self.exam_id=data["exam_id"]
        self.expires_at=data["expires_at"]
        self.end_time=data["end_time"]
        self.entered_room=data["entered_room"]
        self.reservation_time=data["reservation_time"]
        self.exam_document_content_type=data["exam_document_content_type"]
        self.exam_document_file_size=data["exam_document_file_size"]
        self.exam_document_updated_at=data["exam_document_updated_at"]
        self.reviewed=data["reviewed"]
        self.id_card_file_name=data["id_card_file_name"]
        self.id_card_content_type=data["id_card_content_type"]
        self.id_card_file_size=data["id_card_file_size"]
        self.face_photo_file_name=data["face_photo_file_name"]
        self.face_photo_content_type=data["face_photo_content_type"]
        self.face_photo_file_size=data["face_photo_file_size"]
        self.bandwidth_check=data["bandwidth_check"]
        self.bandwidth_speed=data["bandwidth_speed"]
        self.open_time=data["open_time"]
        self.individual_info=data["individual_info"]
        self.rtc_session_id=data["rtc_session_id"]
        self.in_setup=data["in_setup"]
        self.in_check_requirements=data["in_check_requirements"]
        self.attempt=data["attempt"]
        self.archived=data["archived"]
        self.current_exam_mode=data["current_exam_mode"]
        self.rtc_session_ids=data["rtc_session_ids"]
        self.transcoding_status=data["transcoding_status"]
        self.is_individual_info_html=data["is_individual_info_html"]
        self.priority=data["priority"]
        self.recording_started_at=data["recording_started_at"]
        self.recording_ended_at=data["recording_ended_at"]
        self.is_email_sent=data["is_email_sent"]
        self.pod_names=data["pod_names"]
        self.incidents=data["incidents"]
        self.review_commentary=data["review_commentary"]
        self.use_external_service=data["use_external_service"]
        self.incidents_count=data["incidents_count"]
        self.connector=connector

    @staticmethod
    def generate_student_from_response(data, connector=None):
        return Student(data, connector=connector)

    def update(self):
        pass

class StudentList():
    def __init__(self):
        self.__id = 0
        self.__students = []

    def __iter__(self):
        self.__id = 0
        return self

    def __next__(self):
        if self.__id < len(self.__students):
            student = self.__students[self.__id]
            self.__id += 1
            return student
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.__students[key]

    def add (self, student):
        self.__students.append(student)

    def remove_at(self, index):
        self.__students.pop(index)

    def size(self):
        return len(self.__students)
