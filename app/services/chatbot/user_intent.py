#  챗봇 엔진 의도 분류 모듈 생성
import tensorflow as tf
from keras.models import Model, load_model
from keras import preprocessing
from app.services.chatbot.models.intent.IntentModel import IntentedModel
from utils.Preprocess import Preprocess
from config.GlobalParams import MAX_SEQ_LEN


## 의도 분류 모듈 생성
class Intent_Model():
    def __init__(self):
        ## 의도 클래스별 레이블
        self.labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}
        ## 의도 분류 모델 불러오기
        self.model = load_model(r"C:\Users\AIA\PycharmProjects\fastapiProject\app\services\chatbot\models\intent\intent_model.h5")
        ## 챗봇 Proprocess 객체
        self.p = Preprocess

    # 의도 클래스 예측
    def predict_class(self, query):
        ## 형태소 분석
        pos = self.p.pos(query)

        # 문장 내 키워드 추출 및 불용어 제거 후 인덱스로 전환
        keywords = self.p.get_keywords(pos, without_tag=True)
        sequences = [self.p.get_wordix_sequence(keywords)]

        # 단어 시퀀스 벡터 크기


        # 패딩 처리
        padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        # 모델을 활용한 예측, 예측된 값 중 가장 큰 값의 인덱스 반환
        predict = self.model.predict(padded_seqs)
        predict_class = tf.math.argmax(predict, axis=1)

        return predict_class.numpy()[0]

    def intent_test(self):
        p = Preprocess(word2index_dic=r"C:\Users\AIA\PycharmProjects\fastapiProject\app\services\chatbot\train_tools\dict\chatbot_dict.bin",
                       userdic=r"C:\Users\AIA\PycharmProjects\fastapiProject\app\services\chatbot\utils\user_dic.tsv")

        intent = IntentedModel(model_name=r"C:\Users\AIA\PycharmProjects\fastapiProject\app\services\chatbot\models\intent\intent_model.h5", proprocess=p)
        query = "오늘 뭐해?"
        predict = intent.predict_class(query)
        predict_label = intent.labels[predict]

        print(query)
        print("의도 예측 클래스 : ", predict)
        print("의도 예측 레이블 : ", predict_label)

if __name__ == '__main__':
    Intent_Model().intent_test()