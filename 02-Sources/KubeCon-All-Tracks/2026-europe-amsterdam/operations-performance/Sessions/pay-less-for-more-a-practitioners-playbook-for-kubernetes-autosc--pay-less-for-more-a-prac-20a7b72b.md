---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Malgorzata Widelicka", "Lukasz Ogrodowczyk", "Roche"]
sched_url: https://kccnceu2026.sched.com/event/2CW5F/pay-less-for-more-a-practitioners-playbook-for-kubernetes-autoscaling-malgorzata-widelicka-lukasz-ogrodowczyk-roche
youtube_search_url: https://www.youtube.com/results?search_query=Pay+Less+for+More%3A+A+Practitioner%27s+Playbook+for+Kubernetes+Autoscaling+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Pay Less for More: A Practitioner's Playbook for Kubernetes Autoscaling - Malgorzata Widelicka & Lukasz Ogrodowczyk, Roche

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Malgorzata Widelicka, Lukasz Ogrodowczyk, Roche
- Schedule: https://kccnceu2026.sched.com/event/2CW5F/pay-less-for-more-a-practitioners-playbook-for-kubernetes-autoscaling-malgorzata-widelicka-lukasz-ogrodowczyk-roche
- Busca YouTube: https://www.youtube.com/results?search_query=Pay+Less+for+More%3A+A+Practitioner%27s+Playbook+for+Kubernetes+Autoscaling+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Pay Less for More: A Practitioner's Playbook for Kubernetes Autoscaling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW5F/pay-less-for-more-a-practitioners-playbook-for-kubernetes-autoscaling-malgorzata-widelicka-lukasz-ogrodowczyk-roche
- YouTube search: https://www.youtube.com/results?search_query=Pay+Less+for+More%3A+A+Practitioner%27s+Playbook+for+Kubernetes+Autoscaling+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ZRXl6d7Q59g
- YouTube title: Pay Less for More: A Practitioner's Playbook for Kubern... Malgorzata Widelicka & Lukasz Ogrodowczyk
- Match score: 0.796
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/pay-less-for-more-a-practitioners-playbook-for-kubernetes-autoscaling/ZRXl6d7Q59g.txt
- Transcript chars: 21057
- Keywords: infrastructure, carpenter, cost, application, workloads, generally, metrics, cluster, clinical, configuration, minutes, scaling, platform, settings, instances, instance, probably, capacity

### Resumo baseado na transcript

Uh we are a DevOps there and I am specialized in building cloud platform at scale. Um this is my first CubeCon and today together with Mosata we will tell you about the playbook we created based on our experience with Kubernetes and autoscaling. If you are uh working in AWS, we were reaching the security group quotas. And then if you are uh working in multicluster environments, something that is usually troublesome is the maintenance uh upgrade of the Kubernetes also require a lot of manual work. So we moved further and now we provision the infrastructure just for the uh job execution and we scale to zero between those executions to save the money and for us heavy workloads are good candidates for cluster autoscaling and for that we use carpenter uh from version 1.7 carpenter natively support uh reserved capacity and take and takes from this pool in the first order um for cost savings uh when using on demand instances you can consider AWS savings plans >> yeah and if you have some fault

### Excerpt da transcript

My name is Ma Gojata and here is my colleague Gash. >> Hello Kipola. >> We both work at Rush. Uh we are a DevOps there and I am specialized in building cloud platform at scale. >> I've been in IT for 18 years in Rush. I work in pharma R&D division. So it's very high highly regulated environment. Um this is my first CubeCon and today together with Mosata we will tell you about the playbook we created based on our experience with Kubernetes and autoscaling. Uh we are from Rush. ROS is a global pharma company with over 100,000 employees worldwide. It was founded in Basel 130 years ago and uh our company believes that cutting edge science and cutting edge technology can and will improve humans health. >> We both we both work at different project. I am working in envelope platform where we are supporting uh data scientists in a drug discovery process. And to also provide you some numbers um monthly we are generate generating roughly 150 million of predictions and also we are retraining 300 models. >> Uh my platform is called ocean.

It is for ROS data scientist. It is data and analytics platform. It is for GXP and nonGXP clinical trials. So for those of you who are not in pharma, GXP means good practice. It is set of rules and regulations to ensure that clinical data is safe for it. It means that every change should be tested, should be documented and should be traceable. And to give you insights about the scale, we are processing about half pabytes of clinical data and metadata. My team is responsible for the cloud infrastructure and qualification tests. Uh so both those platforms contribute to the drug development journey. >> If you can think about what will happen before the drug will be introduced to the market. So there is a first discovery process. So this is something that I'm supporting. And then clinical trials. So the step that Wukash is supporting. >> Yeah. So we are here to tell you about the issues we had with the infrastructure setup. First pain point is about financial waste. Um paying for readiness instead of executions at and keeping infrastructure ready just in case is waste of money.

The second point is about stability failures frequent out of memory issues um because of lack of proper settings for request and limits. >> Yeah. You may also experience lack of flexibil flexibility. If you would like to introduce for example spot instances, it can be troublesome or require some additional configuration or for example you may reach some quotas.
