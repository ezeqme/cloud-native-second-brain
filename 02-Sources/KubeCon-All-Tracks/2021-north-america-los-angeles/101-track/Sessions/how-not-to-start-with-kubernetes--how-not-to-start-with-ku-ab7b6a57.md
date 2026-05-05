---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "101 Track"
themes: ["Kubernetes Core"]
speakers: ["Christian Heckelmann", "Dynatrace"]
sched_url: https://kccncna2021.sched.com/event/lV1Z/how-not-to-start-with-kubernetes-christian-heckelmann-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=How+NOT+to+Start+with+Kubernetes+CNCF+KubeCon+2021
slides: []
status: parsed
---

# How NOT to Start with Kubernetes - Christian Heckelmann, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[101 Track]]
- Temas: [[Kubernetes Core]]
- País/cidade: United States / Los Angeles
- Speakers: Christian Heckelmann, Dynatrace
- Schedule: https://kccncna2021.sched.com/event/lV1Z/how-not-to-start-with-kubernetes-christian-heckelmann-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=How+NOT+to+Start+with+Kubernetes+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre How NOT to Start with Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV1Z/how-not-to-start-with-kubernetes-christian-heckelmann-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=How+NOT+to+Start+with+Kubernetes+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=c_jruod6L0E
- YouTube title: How NOT to Start with Kubernetes - Christian Heckelmann, Dynatrace
- Match score: 0.754
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/how-not-to-start-with-kubernetes/c_jruod6L0E.txt
- Transcript chars: 24234
- Keywords: cluster, application, workload, running, ingress, network, instance, little, already, deployment, perhaps, clusters, development, beginning, working, deployed, deploy, configuration

### Resumo baseado na transcript

hello everybody and welcome to my talk my session how not to start with kubernetes my name is kristen hegelmann and i want to share with you within the next 30 minutes the lessons i've learned running kubernetes on-prem so on your own data center and it might be a little bit boring for you if you're already running kubernetes because all the things i will mention are basically beginner yeah failures right um so i've splitted this presentation in two parts operation and infrastructure as well as development and

### Excerpt da transcript

hello everybody and welcome to my talk my session how not to start with kubernetes my name is kristen hegelmann and i want to share with you within the next 30 minutes the lessons i've learned running kubernetes on-prem so on your own data center and it might be a little bit boring for you if you're already running kubernetes because all the things i will mention are basically beginner yeah failures right um so i've splitted this presentation in two parts operation and infrastructure as well as development and deployment stuff but let's get started so back in 2018 i was working for another company which was yeah highly regulated and one of our architects reached out to us to the operations team where i was a system engineer and said hey we want to use containers we want to use container orchestration and if we can help him yeah running a small poc and the poc was kubernetes against not against but kubernetes and docker swamp we want to compare both of them both solutions and as i mentioned we need to run on-prem in our case it was based on centos on vmware and xen and it was kubernetes version 1.9 we started with and there's already the first little mistake i made or we made so it was a small poc with a small group of people but when you are building a platform or starting using a platform like kubernetes in your company then you should onboard all other departments as well from the beginning get involved with security get involved with the data center guys like storage and networking guys right because as mentioned you're building a little data center within the data center and the platform will be used by by all of your your developers all of your operation guys so do it in a little bigger scope than you expect and yeah that's the key takeaway here from my perspective and also if you have no idea or no experience running kubernetes then perhaps you should get external help there are companies out there they will take your money and and say what you should do here right so but let's first start with infrastructure and operation topics so as i said our small poc was really um just in my case a three note kubernetes cluster so i provisioned three vms i started installing kubernetes using cube adm manually with sh into the boxes running all the commands right and it was working it was working fine for the first couple of weeks but then i upgraded to kubernetes 1.10 this was also still possible and we hadn't had any storage provision or ingress controllers on
