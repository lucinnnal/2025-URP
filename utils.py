import csv
import json

def csv_to_json(csv_file_path, json_file_path=None):
    """
    CSV 파일을 JSON 형식으로 변환하는 함수

    :param csv_file_path: 입력 CSV 파일 경로 (예: 'data.csv')
    :param json_file_path: 출력 JSON 파일 경로 (예: 'output.json'). None인 경우 파일로 저장하지 않음.
    :return: JSON 형식의 데이터 (딕셔너리)
    """
    json_data = {"video_clips": []}

    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            clip_name = row['filename']
            frame_number = int(row['frame'])
            
            # 키포인트 데이터 추출 (값이 없는 경우 None 처리)
            keypoints = [
                {"name": "Nose", "x": float(row['Nose_x']) if row['Nose_x'] else None, "y": float(row['Nose_y']) if row['Nose_y'] else None},
                {"name": "Neck", "x": float(row['Neck_x']) if row['Neck_x'] else None, "y": float(row['Neck_y']) if row['Neck_y'] else None},
                {"name": "RShoulder", "x": float(row['RShoulder_x']) if row['RShoulder_x'] else None, "y": float(row['RShoulder_y']) if row['RShoulder_y'] else None},
                {"name": "RElbow", "x": float(row['RElbow_x']) if row['RElbow_x'] else None, "y": float(row['RElbow_y']) if row['RElbow_y'] else None},
                {"name": "RWrist", "x": float(row['RWrist_x']) if row['RWrist_x'] else None, "y": float(row['RWrist_y']) if row['RWrist_y'] else None},
                {"name": "LShoulder", "x": float(row['LShoulder_x']) if row['LShoulder_x'] else None, "y": float(row['LShoulder_y']) if row['LShoulder_y'] else None},
                {"name": "LElbow", "x": float(row['LElbow_x']) if row['LElbow_x'] else None, "y": float(row['LElbow_y']) if row['LElbow_y'] else None},
                {"name": "LWrist", "x": float(row['LWrist_x']) if row['LWrist_x'] else None, "y": float(row['LWrist_y']) if row['LWrist_y'] else None},
                {"name": "RHip", "x": float(row['RHip_x']) if row['RHip_x'] else None, "y": float(row['RHip_y']) if row['RHip_y'] else None},
                {"name": "LHip", "x": float(row['LHip_x']) if row['LHip_x'] else None, "y": float(row['LHip_y']) if row['LHip_y'] else None},
                {"name": "REye", "x": float(row['REye_x']) if row['REye_x'] else None, "y": float(row['REye_y']) if row['REye_y'] else None},
                {"name": "LEye", "x": float(row['LEye_x']) if row['LEye_x'] else None, "y": float(row['LEye_y']) if row['LEye_y'] else None},
                {"name": "REar", "x": float(row['REar_x']) if row['REar_x'] else None, "y": float(row['REar_y']) if row['REar_y'] else None},
                {"name": "LEar", "x": float(row['LEar_x']) if row['LEar_x'] else None, "y": float(row['LEar_y']) if row['LEar_y'] else None},
            ]
            
            # 비디오 클립 찾기 또는 생성
            clip_found = False
            for clip in json_data["video_clips"]:
                if clip["clip_name"] == clip_name:
                    clip_found = True
                    clip["frames"].append({
                        "frame_number": frame_number,
                        "keypoints": keypoints
                    })
                    break
            
            # 새로운 비디오 클립 추가
            if not clip_found:
                json_data["video_clips"].append({
                    "clip_name": clip_name,
                    "frames": [{
                        "frame_number": frame_number,
                        "keypoints": keypoints
                    }]
                })

    # JSON 파일로 저장 (json_file_path가 제공된 경우)
    if json_file_path:
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=2)
        print(f"JSON 파일이 {json_file_path}에 저장되었습니다.")

    return json_data