class Student():
    def __init__(self, data, connector=None):
        self.id=data["id"]
        self.session_id=data["session_id"] if "session_id" in data else None
        self.student_id=data["student_id"] if "student_id" in data else None
        self.time_slot=data["time_slot"] if "time_slot" in data else None
        self.created_at=data["created_at"] if "created_at" in data else None
        self.updated_at=data["updated_at"] if "updated_at" in data else None
        self.email=data["email"] if "email" in data else None
        self.pin_code=data["pin_code"] if "pin_code" in data else None
        self.operating_system=data["operating_system"] if "operating_system" in data else None
        self.browser=data["browser"] if "browser" in data else None
        self.browser_version=data["browser_version"] if "browser_version" in data else None
        self.status=data["status"] if "status" in data else None
        self.token=data["token"] if "token" in data else None
        self.screenshare_check=data["screenshare_check"] if "screenshare_check" in data else None
        self.microphone_check=data["microphone_check"] if "microphone_check" in data else None
        self.speakers_check=data["speakers_check"] if "speakers_check" in data else None
        self.webcam_check=data["webcam_check"] if "webcam_check" in data else None
        self.mobile_check=data["mobile_check"] if "mobile_check" in data else None
        self.dummy_exam_survey=data["dummy_exam_survey"] if "dummy_exam_survey" in data else None
        self.skip_requirements=data["skip_requirements"] if "skip_requirements" in data else None
        self.send_confirmation=data["send_confirmation"] if "send_confirmation" in data else None
        self.name=data["name"] if "name" in data else None
        self.start_time=data["start_time"] if "start_time" in data else None
        self.exam_id=data["exam_id"] if "exam_id" in data else None
        self.expires_at=data["expires_at"] if "expires_at" in data else None 
        self.end_time=data["end_time"] if "end_time" in data else None
        self.entered_room=data["entered_room"] if "entered_room" in data else None
        self.reservation_time=data["reservation_time"] if "reservation_time" in data else None 
        self.exam_document_content_type=data["exam_document_content_type"] if "exam_document_content_type" in data else None
        self.exam_document_file_size=data["exam_document_file_size"] if "exam_document_file_size" in data else None
        self.exam_document_updated_at=data["exam_document_updated_at"] if "exam_document_updated_at" in data else None 
        self.reviewed=data["reviewed"] if "reviewed" in data else None
        self.id_card_file_name=data["id_card_file_name"] if "id_card_file_name" in data else None
        self.id_card_content_type=data["id_card_content_type"] if "id_card_content_type" in data else None
        self.id_card_file_size=data["id_card_file_size"] if "id_card_file_size" in data else None
        self.face_photo_file_name=data["face_photo_file_name"] if "face_photo_file_name" in data else None
        self.face_photo_content_type=data["face_photo_content_type"] if "face_photo_content_type" in data else None
        self.face_photo_file_size=data["face_photo_file_size"] if "face_photo_file_size" in data else None
        self.bandwidth_check=data["bandwidth_check"] if "bandwidth_check" in data else None
        self.bandwidth_speed=data["bandwidth_speed"] if "bandwidth_speed" in data else None
        self.open_time=data["open_time"] if "open_time" in data else None
        self.individual_info=data["individual_info"] if "individual_info" in data else None
        self.rtc_session_id=data["rtc_session_id"] if "rtc_session_id" in data else None
        self.in_setup=data["in_setup"] if "in_setup" in data else None
        self.in_check_requirements=data["in_check_requirements"] if "in_check_requirements" in data else None 
        self.attempt=data["attempt"] if "attempt" in data else None
        self.archived=data["archived"] if "archived" in data else None
        self.current_exam_mode=data["current_exam_mode"] if "current_exam_mode" in data else None
        self.rtc_session_ids=data["rtc_session_ids"] if "rtc_session_ids" in data else None
        self.transcoding_status=data["transcoding_status"] if "transcoding_status" in data else None
        self.is_individual_info_html=data["is_individual_info_html"] if "is_individual_info_html" in data else None
        self.priority=data["priority"] if "priority" in data else None
        self.recording_started_at=data["recording_started_at"] if "recording_started_at" in data else None
        self.recording_ended_at=data["recording_ended_at"] if "recording_ended_at" in data else None
        self.is_email_sent=data["is_email_sent"] if "is_email_sent" in data else None
        self.pod_names=data["pod_names"] if "pod_names" in data else None
        self.incidents=data["incidents"] if "incidents" in data else None
        self.review_commentary=data["review_commentary"] if "review_commentary" in data else None
        self.use_external_service=data["use_external_service"] if "use_external_service" in data else None
        self.incidents_count=data["incidents_count"] if "incidents_count" in data else None
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
