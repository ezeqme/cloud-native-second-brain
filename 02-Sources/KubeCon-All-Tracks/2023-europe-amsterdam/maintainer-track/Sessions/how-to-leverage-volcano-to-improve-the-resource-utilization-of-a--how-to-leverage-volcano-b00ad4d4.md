---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["William Wang", "Huawei Cloud"]
sched_url: https://kccnceu2023.sched.com/event/1Hzdd/how-to-leverage-volcano-to-improve-the-resource-utilization-of-ai-pharmaceuticals-autonomous-driving-and-smart-buildings-william-wang-huawei-cloud
youtube_search_url: https://www.youtube.com/results?search_query=How+to+Leverage+Volcano+to+Improve+the+Resource+Utilization+of+AI+Pharmaceuticals%2C+Autonomous+Driving%2C+and+Smart+Buildings+CNCF+KubeCon+2023
slides: []
status: parsed
---

# How to Leverage Volcano to Improve the Resource Utilization of AI Pharmaceuticals, Autonomous Driving, and Smart Buildings - William Wang, Huawei Cloud

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: William Wang, Huawei Cloud
- Schedule: https://kccnceu2023.sched.com/event/1Hzdd/how-to-leverage-volcano-to-improve-the-resource-utilization-of-ai-pharmaceuticals-autonomous-driving-and-smart-buildings-william-wang-huawei-cloud
- Busca YouTube: https://www.youtube.com/results?search_query=How+to+Leverage+Volcano+to+Improve+the+Resource+Utilization+of+AI+Pharmaceuticals%2C+Autonomous+Driving%2C+and+Smart+Buildings+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre How to Leverage Volcano to Improve the Resource Utilization of AI Pharmaceuticals, Autonomous Driving, and Smart Buildings.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hzdd/how-to-leverage-volcano-to-improve-the-resource-utilization-of-ai-pharmaceuticals-autonomous-driving-and-smart-buildings-william-wang-huawei-cloud
- YouTube search: https://www.youtube.com/results?search_query=How+to+Leverage+Volcano+to+Improve+the+Resource+Utilization+of+AI+Pharmaceuticals%2C+Autonomous+Driving%2C+and+Smart+Buildings+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ujHDV5xteqU
- YouTube title: How to Leverage Volcano to Improve the Resource Utilization of AI Pharmaceuticals... - William Wang
- Match score: 0.893
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/how-to-leverage-volcano-to-improve-the-resource-utilization-of-ai-phar/ujHDV5xteqU.txt
- Transcript chars: 19458
- Keywords: volcano, scheduling, support, scheduler, resources, resource, cluster, workload, currently, utilization, training, computing, improve, multiple, submit, running, platform, results

### Resumo baseado na transcript

uh good afternoon uh I'm I'm William Wong from Huawei cloud and I'm a mentor of volcano community and in last 20 years I have been working on the traditional software hpcs software development and the air and big data on kubernetes so today my topic is how to leverage your candle to improve the resource utilization for kubernetes cluster so I'm going to but firstly I'm going to talk about the volcano project and then I like to talk about the architectural volcano and how it works in kubernetes another use case is is about a new platform this this Enterprise use the AI and the molecular simulation algorithm to create Next Generation macro skill industry design and simulation platform for energy material and research so their goal is their goal is to achieve high performance Computing based on the multi-cubernetes cluster and the traditionally slurm cluster so the requirement is is all of these kubernetes cluster is distributed in different regions it's difficult to maintain and also the drug the the drug Discovery workload requires massive massive compute

### Excerpt da transcript

uh good afternoon uh I'm I'm William Wong from Huawei cloud and I'm a mentor of volcano community and in last 20 years I have been working on the traditional software hpcs software development and the air and big data on kubernetes so today my topic is how to leverage your candle to improve the resource utilization for kubernetes cluster so I'm going to but firstly I'm going to talk about the volcano project and then I like to talk about the architectural volcano and how it works in kubernetes after that I'm going to talk about the new challenges and some features and finally I will show you several use cases to show you how volcano help users to to improve their job in performance and the resource utilization okay so what kind of project is open source the in 2019 and opens and that donated by Huawei to cncf in 2020 2020 and currently we have more than 500 computers all over the world and more than 50 Enterprise users have adopted volcano in their production environment and for this month we will release the the 24th version here we can see a volcano project has strong relationship with the Upstream Computing framework such such as the sparkling in big data and the flow MPI and pathology Etc so we currently we support most of these Computing Frameworks efficiently and here we can see volcano is not just a scheduler it has the job controller to con to control the enhanced job lifecycle management and supports the multiple code template and also it has the the Q to help users to share resources for much tenant and we hope we and we also support the uh the scheduler enhance the scheduler and supported the just likely topology business scheduling uh gun scheduling and preemption and backfill for the analyzing Hardware we are working with with kubernetes to support the more kind of heterogeneous devices like s86 um GTO MTU and kunlean and also for the common law we also developed a variety of command line to cover traditionally HTC users to microgreens from this form of HTC to kubernetes mostly here we can here we can have look about the volcano scheduler architecture so volcano support area and Big Data through the job-based scheduling and the plugin magnesium so basically there are three parts in the volcano scheduler the first part is the the catch so the cash is watching the Google API server and build the job and task relationship based on the code group and code and for the issue easy trick scheduling cycle as as we all know in distributed system is is v
