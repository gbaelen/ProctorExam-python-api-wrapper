class Student():
    def __init__(self, id=None, session_id=None, student_id=None, time_slot=None, created_at=None, updated_at=None, email="", pin_code=None, operating_system=None, browser=None, browser_version=None, status=None, token=None, screenshare_check=None, microphone_check=None, speakers_check=None, webcam_check=None, mobile_check=None, dummy_exam_survey=None, skip_requirements=None, send_confirmation=None, name=None, start_time=None, exam_id=None, expires_at=None, end_time=None, entered_room=None, reservation_time=None, exam_document_content_type=None, exam_document_file_size=None, exam_document_updated_at=None, reviewed=None, id_card_file_name=None, id_card_content_type=None, id_card_file_size=None, face_photo_file_name=None, face_photo_content_type=None, face_photo_file_size=None, bandwidth_check=None, bandwidth_speed=None, open_time=None, individual_info=None, rtc_session_id=None, in_setup=None, in_check_requirements=None, attempt=None, archived=None, current_exam_mode=None, rtc_session_ids=[], transcoding_status=None, is_individual_info_html=None, priority=None, recording_started_at=None, recording_ended_at=None, is_email_sent=None, pod_names=[], incidents=[], review_commentary=None, use_external_service=None, incidents_count=None, connector=None):
        self.id=id
        self.session_id=session_id
        self.student_id=student_id
        self.time_slot=time_slot
        self.created_at=created_at
        self.updated_at=updated_at
        self.email=email
        self.pin_code=pin_code
        self.operating_system=operating_system
        self.browser=browser
        self.browser_version=browser_version
        self.status=status
        self.token=token
        self.screenshare_check=screenshare_check
        self.microphone_check=microphone_check
        self.speakers_check=speakers_check
        self.webcam_check=webcam_check
        self.mobile_check=mobile_check
        self.dummy_exam_survey=dummy_exam_survey
        self.skip_requirements=skip_requirements
        self.send_confirmation=send_confirmation
        self.name=name
        self.start_time=start_time
        self.exam_id=exam_id
        self.expires_at=expires_at
        self.end_time=end_time
        self.entered_room=entered_room
        self.reservation_time=reservation_time
        self.exam_document_content_type=exam_document_content_type
        self.exam_document_file_size=exam_document_file_size
        self.exam_document_updated_at=exam_document_updated_at
        self.reviewed=reviewed
        self.id_card_file_name=id_card_file_name
        self.id_card_content_type=id_card_content_type
        self.id_card_file_size=id_card_file_size
        self.face_photo_file_name=face_photo_file_name
        self.face_photo_content_type=face_photo_content_type
        self.face_photo_file_size=face_photo_file_size
        self.bandwidth_check=bandwidth_check
        self.bandwidth_speed=bandwidth_speed
        self.open_time=open_time
        self.individual_info=individual_info
        self.rtc_session_id=rtc_session_id
        self.in_setup=in_setup
        self.in_check_requirements=in_check_requirements
        self.attempt=attempt
        self.archived=archived
        self.current_exam_mode=current_exam_mode
        self.rtc_session_ids=rtc_session_ids
        self.transcoding_status=transcoding_status
        self.is_individual_info_html=is_individual_info_html
        self.priority=priority
        self.recording_started_at=recording_started_at
        self.recording_ended_at=recording_ended_at
        self.is_email_sent=is_email_sent
        self.pod_names=pod_names
        self.incidents=incidents
        self.review_commentary=review_commentary
        self.use_external_service=use_external_service
        self.incidents_count=incidents_count
        self.connector=connector

    @staticmethod
    def generate_student_from_response(data, connector=None):
        return Student(**data, connector=connector)

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
