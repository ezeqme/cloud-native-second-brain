---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["William Wang", "Huawei Cloud"]
sched_url: https://kccncna2022.sched.com/event/182Na/intro-to-volcano-cloud-native-batch-system-william-wang-huawei-cloud
youtube_search_url: https://www.youtube.com/results?search_query=Intro+To+Volcano%3A+Cloud+Native+Batch+System+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Intro To Volcano: Cloud Native Batch System - William Wang, Huawei Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: William Wang, Huawei Cloud
- Schedule: https://kccncna2022.sched.com/event/182Na/intro-to-volcano-cloud-native-batch-system-william-wang-huawei-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=Intro+To+Volcano%3A+Cloud+Native+Batch+System+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Intro To Volcano: Cloud Native Batch System.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Na/intro-to-volcano-cloud-native-batch-system-william-wang-huawei-cloud
- YouTube search: https://www.youtube.com/results?search_query=Intro+To+Volcano%3A+Cloud+Native+Batch+System+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=xASlauMw2Bc
- YouTube title: Intro To Volcano: Cloud Native Batch System - William Wang, Huawei Cloud
- Match score: 0.844
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/intro-to-volcano-cloud-native-batch-system/xASlauMw2Bc.txt
- Transcript chars: 13626
- Keywords: scheduling, resources, volcano, computing, resource, support, management, workload, scenarios, coding, cluster, gpu, multiple, training, volano, provides, scenario, introduce

### Resumo baseado na transcript

hello everyone I'm William from Huawei today I I'd like to introduce Cloud native batch system Cano to you guys so the talk basically comes up with four parts the first one is volcano brief then the new scenarios and that we are exploring this year after that we will go through the community updates and also the release volcano is started in 2019 targeting on providing the extending kubernetes and cative Technologies to the badge Computing the project was donated to cncf in 2019 and this year we moved

### Excerpt da transcript

hello everyone I'm William from Huawei today I I'd like to introduce Cloud native batch system Cano to you guys so the talk basically comes up with four parts the first one is volcano brief then the new scenarios and that we are exploring this year after that we will go through the community updates and also the release volcano is started in 2019 targeting on providing the extending kubernetes and cative Technologies to the badge Computing the project was donated to cncf in 2019 and this year we moved to incubation level volano release a feature version every 3 months now the community have around two and 2.6 s gate half star stars and 640 Forks since joining CCF we received over 450 contributors from all over the world from the graph we can also see that we canot engage deeply with Upstream Computing Frameworks so far we we have supported almost all of the mainstream Computing framework for the public adoption we do get lot of user users especially for people are running big AI Big Data gen contast coding workload on kubernetes here are part of adopters using volcano in production environment actually you can see there's very good diversity over the industry we have adopters from internet companies also there are Financial companies cloud provider and Gene Computing related companies current currently more than 50 companies adopt volcano in their production environment as the figure shows volcano is not just a scheduler first of all volano provides some core apis such as job q and P group on the basis of kubernetes which are convenient for defining batch work workflows and controlling the process of resource allocation secondly the volcano scheduler component provides Rich batch scheduling algorithm such as F A topology s preempt and backfield elastic scheduling to improve the job performance at the same time the plugin scheduling framework allow user to Define their own customized orgism the volcano controller component consists of three controllers job controller Q controller and put group controller the job controller is used to management the job declaration and left cycle management and the Q controller provides resource sharing in M mendance scenario such as Q proportion Q me me and Max Capacity on the notes we can provides support for heterogenous Hardware such as support such as x86 arm GPU mpu Etc as well as resource topology and isolation capabilities in the future we will also support C related related capabilities let's take a look at stereoty
