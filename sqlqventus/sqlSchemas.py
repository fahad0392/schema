CREATE_LABS = """
create table encounter_master(
	id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	hospital integer NOT NULL REFERENCES main_hospital (id),
	instance1 varchar(128),
	instance2 varchar(128),
	instance3 varchar(128),
	instance5 varchar(128),
	first_name varchar(128),
	middle_name varchar(128),
	last_name varchar(128),
	gender varchar(16),
	language varchar(128),
	interpreter varchar(16),
	primary_race varchar(128),
	home_zip_code integer,
	home_country varchar(128),
	payor varchar(128),
	payor_type varchar(128),
	age integer,
	height float,
	weight float,
	record_created_time datetime,
	arrival_time datetime,
	admit_time datetime,
	admit_order_time datetime,
	admit_user varchar(128),
	admitting_service varchar(128),
	arriving_class varchar(128),
	admitting_diagnosis varchar(128),
	admitting_dx_code varchar(128),
	discharge_time datetime,
	discharge_enter_time datetime,
	discharge_provider varchar(128),
	discharge_user varchar(128),
	discharge_order_time datetime,
	discharge_order_user varchar(128),
	patient_class varchar(64),
	patient_class_mapped varchar(64),
	admitting_provider varchar(128),
	attending_provider varchar(128),
	discharge_nurse varchar(128),
	service varchar(128),
	admitting_department varchar(128),
	current_department varchar(128),
	current_bed varchar(128),
	admit_source varchar(128),
	admit_source_map varchar(128),
	discharge_disposition varchar(128),
	discharge_disposition_map varchar(128),
	principle_icd10_code varchar(128),
	principle_icd10_name varchar(128),
	mom_instance2 varchar(128),
	final_drg_code varchar(32),
	final_drg_name varchar(512),
	final_drg_gmlos float,
	qv_created_src varchar(128),
	qv_created_ts timestamp default current_timestamp,
	qv_updated_src varchar(128),
	qv_updated_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP


);
CREATE UNIQUE INDEX instance_index ON encounter_master (hospital, instance2);

create table med_admin(
	id integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
	hospital integer NOT NULL REFERENCES main_hospital (id),
	instance1 varchar(128),
	instance2 varchar(128),
	instance3 varchar(128),
	instance5 varchar(128),
	admin_event_id varchar(128),
	order_id varchar(128),
	internal_med_id varchar(128),
	med_name varchar(128),
	ndc_code varchar(128),
	dose_given varchar(128),
	dose_route varchar(128),
	admin_name varchar(128),
	admin_id varchar(128),
	admin_role varchar(128),
	admin_event_type varchar(128),
	admin_event_time datetime,
	admin_due_time datetime,
	admin_verify_time datetime,
	admin_verify_user varchar(128),
	barcode_scan varchar(128),
	qv_created_src varchar(128),
	qv_created_ts timestamp default current_timestamp,
	qv_updated_src varchar(128),
	qv_updated_ts timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
CREATE UNIQUE index instance_index on med_admin(hospital, order_id, admin_event_id);
CREATE index instance1_index on med_admin(hospital, instance1);

CREATE index instance2_index on med_admin(hospital, instance2);

CREATE index instance3_index on med_admin(hospital, instance3);

CREATE index admin_event_time_index on med_admin(hospital, admin_event_time);

CREATE index med_name_index on med_admin(hospital, med_name);
"""
