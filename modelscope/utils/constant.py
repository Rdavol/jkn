# Copyright (c) Alibaba, Inc. and its affiliates.
import enum


class Fields(object):
    """ Names for different application fields
    """
    cv = 'cv'
    nlp = 'nlp'
    audio = 'audio'
    multi_modal = 'multi-modal'


class CVTasks(object):
    # ocr
    ocr_detection = 'ocr-detection'
    ocr_recognition = 'ocr-recognition'

    # human face body related
    animal_recognition = 'animal-recognition'
    face_detection = 'face-detection'
    face_recognition = 'face-recognition'
    facial_expression_recognition = 'facial-expression-recognition'
    face_2d_keypoints = 'face-2d-keypoints'
    human_detection = 'human-detection'
    human_object_interaction = 'human-object-interaction'
    face_image_generation = 'face-image-generation'
    body_2d_keypoints = 'body-2d-keypoints'
    body_3d_keypoints = 'body-3d-keypoints'
    hand_2d_keypoints = 'hand-2d-keypoints'
    general_recognition = 'general-recognition'

    image_classification = 'image-classification'
    image_multilabel_classification = 'image-multilabel-classification'
    image_classification_imagenet = 'image-classification-imagenet'
    image_classification_dailylife = 'image-classification-dailylife'

    image_object_detection = 'image-object-detection'

    image_segmentation = 'image-segmentation'
    portrait_matting = 'portrait-matting'
    text_driven_segmentation = 'text-driven-segmentation'
    shop_segmentation = 'shop-segmentation'

    # image editing
    skin_retouching = 'skin-retouching'
    image_super_resolution = 'image-super-resolution'
    image_colorization = 'image-colorization'
    image_color_enhancement = 'image-color-enhancement'
    image_denoising = 'image-denoising'
    image_portrait_enhancement = 'image-portrait-enhancement'

    # image generation
    image_to_image_translation = 'image-to-image-translation'
    image_to_image_generation = 'image-to-image-generation'
    image_style_transfer = 'image-style-transfer'
    image_portrait_stylization = 'image-portrait-stylization'

    image_embedding = 'image-embedding'

    product_retrieval_embedding = 'product-retrieval-embedding'

    # video recognition
    live_category = 'live-category'
    action_recognition = 'action-recognition'
    action_detection = 'action-detection'
    video_category = 'video-category'
    video_embedding = 'video-embedding'
    virtual_try_on = 'virtual-try-on'
    crowd_counting = 'crowd-counting'
    movie_scene_segmentation = 'movie-scene-segmentation'

    # video editing
    video_inpainting = 'video-inpainting'

    # reid and tracking
    video_single_object_tracking = 'video-single-object-tracking'
    video_summarization = 'video-summarization'
    image_reid_person = 'image-reid-person'


class NLPTasks(object):
    # nlp tasks
    word_segmentation = 'word-segmentation'
    part_of_speech = 'part-of-speech'
    named_entity_recognition = 'named-entity-recognition'
    nli = 'nli'
    sentiment_classification = 'sentiment-classification'
    sentiment_analysis = 'sentiment-analysis'
    sentence_similarity = 'sentence-similarity'
    text_classification = 'text-classification'
    sentence_embedding = 'sentence-embedding'
    passage_ranking = 'passage-ranking'
    relation_extraction = 'relation-extraction'
    zero_shot = 'zero-shot'
    translation = 'translation'
    token_classification = 'token-classification'
    conversational = 'conversational'
    text_generation = 'text-generation'
    task_oriented_conversation = 'task-oriented-conversation'
    dialog_intent_prediction = 'dialog-intent-prediction'
    dialog_state_tracking = 'dialog-state-tracking'
    table_question_answering = 'table-question-answering'
    sentence_embedding = 'sentence-embedding'
    fill_mask = 'fill-mask'
    summarization = 'summarization'
    question_answering = 'question-answering'
    zero_shot_classification = 'zero-shot-classification'
    backbone = 'backbone'
    text_error_correction = 'text-error-correction'
    faq_question_answering = 'faq-question-answering'
    conversational_text_to_sql = 'conversational-text-to-sql'
    information_extraction = 'information-extraction'
    document_segmentation = 'document-segmentation'


class AudioTasks(object):
    # audio tasks
    auto_speech_recognition = 'auto-speech-recognition'
    text_to_speech = 'text-to-speech'
    speech_signal_process = 'speech-signal-process'
    acoustic_echo_cancellation = 'acoustic-echo-cancellation'
    acoustic_noise_suppression = 'acoustic-noise-suppression'
    keyword_spotting = 'keyword-spotting'


class MultiModalTasks(object):
    # multi-modal tasks
    image_captioning = 'image-captioning'
    visual_grounding = 'visual-grounding'
    text_to_image_synthesis = 'text-to-image-synthesis'
    multi_modal_embedding = 'multi-modal-embedding'
    generative_multi_modal_embedding = 'generative-multi-modal-embedding'
    multi_modal_similarity = 'multi-modal-similarity'
    visual_question_answering = 'visual-question-answering'
    visual_entailment = 'visual-entailment'
    video_multi_modal_embedding = 'video-multi-modal-embedding'
    image_text_retrieval = 'image-text-retrieval'


class TasksIODescriptions(object):
    image_to_image = 'image_to_image',
    images_to_image = 'images_to_image',
    image_to_text = 'image_to_text',
    seed_to_image = 'seed_to_image',
    text_to_speech = 'text_to_speech',
    text_to_text = 'text_to_text',
    speech_to_text = 'speech_to_text',
    speech_to_speech = 'speech_to_speech'
    speeches_to_speech = 'speeches_to_speech',
    visual_grounding = 'visual_grounding',
    visual_question_answering = 'visual_question_answering',
    visual_entailment = 'visual_entailment',
    generative_multi_modal_embedding = 'generative_multi_modal_embedding'


class Tasks(CVTasks, NLPTasks, AudioTasks, MultiModalTasks):
    """ Names for tasks supported by modelscope.

    Holds the standard task name to use for identifying different tasks.
    This should be used to register models, pipelines, trainers.
    """
    reverse_field_index = {}

    @staticmethod
    def find_field_by_task(task_name):
        if len(Tasks.reverse_field_index) == 0:
            # Lazy init, not thread safe
            field_dict = {
                Fields.cv: [
                    getattr(Tasks, attr) for attr in dir(CVTasks)
                    if not attr.startswith('__')
                ],
                Fields.nlp: [
                    getattr(Tasks, attr) for attr in dir(NLPTasks)
                    if not attr.startswith('__')
                ],
                Fields.audio: [
                    getattr(Tasks, attr) for attr in dir(AudioTasks)
                    if not attr.startswith('__')
                ],
                Fields.multi_modal: [
                    getattr(Tasks, attr) for attr in dir(MultiModalTasks)
                    if not attr.startswith('__')
                ],
            }

            for field, tasks in field_dict.items():
                for task in tasks:
                    if task in Tasks.reverse_field_index:
                        raise ValueError(f'Duplicate task: {task}')
                    Tasks.reverse_field_index[task] = field

        return Tasks.reverse_field_index.get(task_name)


class InputFields(object):
    """ Names for input data fields in the input data for pipelines
    """
    img = 'img'
    text = 'text'
    audio = 'audio'


class Hubs(enum.Enum):
    """ Source from which an entity (such as a Dataset or Model) is stored
    """
    modelscope = 'modelscope'
    huggingface = 'huggingface'


class DownloadMode(enum.Enum):
    """ How to treat existing datasets
    """
    REUSE_DATASET_IF_EXISTS = 'reuse_dataset_if_exists'
    FORCE_REDOWNLOAD = 'force_redownload'


class DatasetFormations(enum.Enum):
    """ How a dataset is organized and interpreted
    """
    # formation that is compatible with official huggingface dataset, which
    # organizes whole dataset into one single (zip) file.
    hf_compatible = 1
    # native modelscope formation that supports, among other things,
    # multiple files in a dataset
    native = 2


DatasetMetaFormats = {
    DatasetFormations.native: ['.json'],
    DatasetFormations.hf_compatible: ['.py'],
}


class ModelFile(object):
    CONFIGURATION = 'configuration.json'
    README = 'README.md'
    TF_SAVED_MODEL_FILE = 'saved_model.pb'
    TF_GRAPH_FILE = 'tf_graph.pb'
    TF_CHECKPOINT_FOLDER = 'tf_ckpts'
    TF_CKPT_PREFIX = 'ckpt-'
    TORCH_MODEL_FILE = 'pytorch_model.pt'
    TORCH_MODEL_BIN_FILE = 'pytorch_model.bin'
    VOCAB_FILE = 'vocab.txt'
    ONNX_MODEL_FILE = 'model.onnx'
    LABEL_MAPPING = 'label_mapping.json'
    TRAIN_OUTPUT_DIR = 'output'


class ConfigFields(object):
    """ First level keyword in configuration file
    """
    framework = 'framework'
    task = 'task'
    pipeline = 'pipeline'
    model = 'model'
    dataset = 'dataset'
    preprocessor = 'preprocessor'
    train = 'train'
    evaluation = 'evaluation'


class ConfigKeys(object):
    """Fixed keywords in configuration file"""
    train = 'train'
    val = 'val'


class Requirements(object):
    """Requirement names for each module
    """
    protobuf = 'protobuf'
    sentencepiece = 'sentencepiece'
    sklearn = 'sklearn'
    scipy = 'scipy'
    timm = 'timm'
    tokenizers = 'tokenizers'
    tf = 'tf'
    torch = 'torch'


class Frameworks(object):
    tf = 'tensorflow'
    torch = 'pytorch'
    kaldi = 'kaldi'


DEFAULT_MODEL_REVISION = 'master'
DEFAULT_DATASET_REVISION = 'master'
DEFAULT_DATASET_NAMESPACE = 'modelscope'


class ModeKeys:
    TRAIN = 'train'
    EVAL = 'eval'
    INFERENCE = 'inference'


class LogKeys:
    ITER = 'iter'
    ITER_TIME = 'iter_time'
    EPOCH = 'epoch'
    LR = 'lr'  # learning rate
    MODE = 'mode'
    DATA_LOAD_TIME = 'data_load_time'
    ETA = 'eta'  # estimated time of arrival
    MEMORY = 'memory'
    LOSS = 'loss'


class TrainerStages:
    before_run = 'before_run'
    before_train_epoch = 'before_train_epoch'
    before_train_iter = 'before_train_iter'
    after_train_iter = 'after_train_iter'
    after_train_epoch = 'after_train_epoch'
    before_val_epoch = 'before_val_epoch'
    before_val_iter = 'before_val_iter'
    after_val_iter = 'after_val_iter'
    after_val_epoch = 'after_val_epoch'
    after_run = 'after_run'


class ColorCodes:
    MAGENTA = '\033[95m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'


class Devices:
    """device used for training and inference"""
    cpu = 'cpu'
    gpu = 'gpu'
