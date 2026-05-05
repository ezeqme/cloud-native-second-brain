---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Machine Learning + Data"
themes: ["AI ML", "Storage Data"]
speakers: ["Jihye Choi", "SAMSUNG SDS"]
sched_url: https://kccncna2022.sched.com/event/182Fq/machine-learning-using-various-gpu-technology-with-kubeflow-jihye-choi-samsung-sds
youtube_search_url: https://www.youtube.com/results?search_query=Machine+Learning+Using+Various+GPU+Technology+With+Kubeflow.+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Machine Learning Using Various GPU Technology With Kubeflow. - Jihye Choi, SAMSUNG SDS

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Machine Learning + Data]]
- Temas: [[AI ML]], [[Storage Data]]
- País/cidade: United States / Detroit
- Speakers: Jihye Choi, SAMSUNG SDS
- Schedule: https://kccncna2022.sched.com/event/182Fq/machine-learning-using-various-gpu-technology-with-kubeflow-jihye-choi-samsung-sds
- Busca YouTube: https://www.youtube.com/results?search_query=Machine+Learning+Using+Various+GPU+Technology+With+Kubeflow.+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Machine Learning Using Various GPU Technology With Kubeflow..

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Fq/machine-learning-using-various-gpu-technology-with-kubeflow-jihye-choi-samsung-sds
- YouTube search: https://www.youtube.com/results?search_query=Machine+Learning+Using+Various+GPU+Technology+With+Kubeflow.+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=VZGsBgvB1KQ
- YouTube title: Machine Learning Using Various GPU Technology With Kubeflow. - Jihye Choi, SAMSUNG SDS
- Match score: 0.917
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/machine-learning-using-various-gpu-technology-with-kubeflow/VZGsBgvB1KQ.txt
- Transcript chars: 19493
- Keywords: gpu, device, training, distributed, memory, machine, direct, learning, network, performance, technology, platform, resource, executed, communication, environment, jupiter, without

### Resumo baseado na transcript

okay hello everyone good afternoon uh I'm jih Che from Korea and I'd like to thank everyone for participating in today's presentation despite your busy schedules uh I am working at Samsung S6 as an infra item I'm sorry I am uh I have been working at Samsung SDS as an infra architect for about seven years and as a cloud architect for the recent three years having particular uh interested in open source including kubernetes and Cuba flow and I'm also proceeding with a various POC to develop the the record case study I'd like to introduce POC with related to review director RDMA technology as the size of the model gets bigger and the amount of the data is increases to enhance the accuracy of deep learning we need countries the computers and efficient distributed processing I'm going to explain GPU direct RDMA technology for working out of GPU distributed training and system architecture as well as some examples and share the performance the verification result first of all GPU art direct RDMA is a function that allows

### Excerpt da transcript

okay hello everyone good afternoon uh I'm jih Che from Korea and I'd like to thank everyone for participating in today's presentation despite your busy schedules uh I am working at Samsung S6 as an infra item I'm sorry I am uh I have been working at Samsung SDS as an infra architect for about seven years and as a cloud architect for the recent three years having particular uh interested in open source including kubernetes and Cuba flow and I'm also proceeding with a various POC to develop the best machine learning platform focusing on the components like Network server and GPU and applied it to service based on my experiences as an infra architect my team is currently developing a machine learning platform which is based on Kiva flow and at the beginning of this year we add on the functions uh that for enhancing the usability to qf flow which is on Samsung SDS Cloud platform and release a keyword flow service which is consistently being updated uh for those of you who are not familiar with SSP Samsung Cloud platform is a cloud environment launched by Samsung SDS in July last year which what virtualizes and provide buys various components like Computing stories and database that are necessary for corporations corporate Cloud can be used conveniently as a self-service and it provides a very high quality availability and stability as I mentioned earlier my team developed a keyword flow service on this sap through our experience of developing a machine learning platform we've learned a lot I assume that those from the field of machine learning Ai and Mr office would agree with me on this the biggest lesson that we learned the on The Limited cost and how important it was to utilize the GPU within that cost so I'd like to introduce two cases stories on how we improve to improve that part and applied it to our platform service yes first of all for those who are not familiar with the Cuba flow it is a machine learning are toolkit based on kubernetes and its open source projects and that enables the simple scaling of motion machine learning model and deployment to production qf Pro provides various components like Jupiter notebook captive or pipelines and training operators that allowing data scientists and machine learning Engineers to work on machine learning training high performance parameter tuning and serving workflow however the components that uh process process effective distributed training by combining with GPU ecosystem or maximize the GPU utilization r
