---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data"]
speakers: ["Ti Zhou", "Baidu", "William Wang", "Huawei"]
sched_url: https://kccnceu2021.sched.com/event/iE3R/optimizing-knowledge-distillation-training-with-volcano-ti-zhou-baidu-william-wang-huawei
youtube_search_url: https://www.youtube.com/results?search_query=Optimizing+Knowledge+Distillation+Training+With+Volcano+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Optimizing Knowledge Distillation Training With Volcano - Ti Zhou, Baidu & William Wang, Huawei

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: Virtual / Virtual
- Speakers: Ti Zhou, Baidu, William Wang, Huawei
- Schedule: https://kccnceu2021.sched.com/event/iE3R/optimizing-knowledge-distillation-training-with-volcano-ti-zhou-baidu-william-wang-huawei
- Busca YouTube: https://www.youtube.com/results?search_query=Optimizing+Knowledge+Distillation+Training+With+Volcano+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Optimizing Knowledge Distillation Training With Volcano.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE3R/optimizing-knowledge-distillation-training-with-volcano-ti-zhou-baidu-william-wang-huawei
- YouTube search: https://www.youtube.com/results?search_query=Optimizing+Knowledge+Distillation+Training+With+Volcano+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cDPGmhVcj7Y
- YouTube title: Optimizing Knowledge Distillation Training With Volcano - Ti Zhou, Baidu & William Wang, Huawei
- Match score: 0.844
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/optimizing-knowledge-distillation-training-with-volcano/cDPGmhVcj7Y.txt
- Transcript chars: 22530
- Keywords: training, teacher, distillation, volcano, resources, student, scheduling, cluster, workload, resource, knowledge, network, performance, gpu, results, online, submit, method

### Resumo baseado na transcript

hi everyone welcome to our session today this is t zhao from baidu and label one from huawei we will introduce how to optimize the knowledge distillation training with volcano thanks next slide okay so let's have a quick overview of the project's background pilot paddle is china's fully open source deep learning platform and it is also an agile framework for industrial development of deep neural networks palo palo deep learning framework supports both declarative programming and imperative programming with both development flexibility and a high runtime performance preserved

### Excerpt da transcript

hi everyone welcome to our session today this is t zhao from baidu and label one from huawei we will introduce how to optimize the knowledge distillation training with volcano thanks next slide okay so let's have a quick overview of the project's background pilot paddle is china's fully open source deep learning platform and it is also an agile framework for industrial development of deep neural networks palo palo deep learning framework supports both declarative programming and imperative programming with both development flexibility and a high runtime performance preserved pilot paddle also support ultra large scale training of deep neural networks it launched the worst the world's first large-scale open source training platform that supports the training of deep network with 100 billion of features and trillions of parameters using data source distributed over hundreds of nodes piloped includes and maintains more than 100 mainstream models that have been practically and polished for a long time in the industry some of these models have one major price from well-known industrial competitions in the meanwhile palo pado has more than 200 pre-trained models to facilitate the rapid development of industrial applications next slide for large scale training pilot pedal enabled collective training on multiple gpus also supports the asynchronized parameter server mode training on gpu and cpus pilot header used bleach api for highly scalable distributed training and now most of the baidual intelligence services are powered by pedophile framework when pilot pedal do the large-scale distributed training inside baidu we suffer from some problems one is uh when one of the products in the large distributed job got failed the whole job failed it will waste a lot of resources to restart the whole job another one is the low utilization of some influence card cluster like k-40 while the training card cluster like v100 is always out of resources so we need to figure out a way to resolve those two main problems when training in the large kubernetes cluster next slide okay we create edl project uh the elastic deep learning project as the middle layer between kubernetes and pilot paddle framework to handle the elastic training related stuff currently edr uses kubernetes as the foundation and provides user scenarios including predictive training methods like knowledge distillation reinforced learning and hyper primary search by using the kubernetes crd and now with three major
