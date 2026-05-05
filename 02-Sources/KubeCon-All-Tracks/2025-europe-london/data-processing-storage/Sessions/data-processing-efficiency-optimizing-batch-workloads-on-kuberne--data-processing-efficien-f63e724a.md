---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Hichem Kenniche", "Independent"]
sched_url: https://kccnceu2025.sched.com/event/1tx8p/data-processing-efficiency-optimizing-batch-workloads-on-kubernetes-with-custom-schedulers-hichem-kenniche-independent
youtube_search_url: https://www.youtube.com/results?search_query=Data+Processing+Efficiency%3A+Optimizing+Batch+Workloads+on+Kubernetes+With+Custom+Schedulers+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Data Processing Efficiency: Optimizing Batch Workloads on Kubernetes With Custom Schedulers - Hichem Kenniche, Independent

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Hichem Kenniche, Independent
- Schedule: https://kccnceu2025.sched.com/event/1tx8p/data-processing-efficiency-optimizing-batch-workloads-on-kubernetes-with-custom-schedulers-hichem-kenniche-independent
- Busca YouTube: https://www.youtube.com/results?search_query=Data+Processing+Efficiency%3A+Optimizing+Batch+Workloads+on+Kubernetes+With+Custom+Schedulers+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Data Processing Efficiency: Optimizing Batch Workloads on Kubernetes With Custom Schedulers.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8p/data-processing-efficiency-optimizing-batch-workloads-on-kubernetes-with-custom-schedulers-hichem-kenniche-independent
- YouTube search: https://www.youtube.com/results?search_query=Data+Processing+Efficiency%3A+Optimizing+Batch+Workloads+on+Kubernetes+With+Custom+Schedulers+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BkQRGsVBhkc
- YouTube title: Data Processing Efficiency: Optimizing Batch Workloads on Kubernetes With Custom... Hichem Kenniche
- Match score: 0.988
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/data-processing-efficiency-optimizing-batch-workloads-on-kubernetes-wi/BkQRGsVBhkc.txt
- Transcript chars: 24064
- Keywords: scheduling, important, amazing, resources, volcano, around, default, application, hopefully, priority, workloads, another, resource, engineering, already, platform, apache, cluster

### Resumo baseado na transcript

So data engineering, machine learning engineering, we come from another word, Hadoop word, and it's probably dead already. We struggled at the beginning a lot especially that I mean Kubernetes was built for stateless. I've seen in the three days I was really depressed because it's Gen AI everywhere and this was like you know oldfashioned machine learning predictive machine learning. like you know testimonies from Apple I guess from migrating from Hadoop to Kubernetes so we had in the past a standalone MSO uh yarn which is still widely used yarn is important because it's we at least got uh inspiration from there and then finally uh Kubernetes which is you know the the most popular one and it's and I think objectively is the the right way of deploying spark. That's the kind of key thing and hopefully like you know we can more and more talk about this how can I use efficiently my infrastructure and the result will be cost reduction and also will be you know energy reduction footprint uh carbon footprint reduction etc.

### Excerpt da transcript

Hello everyone. Uh thank you for joining this maybe last session. I heard that they kept the best for the last. So really excited and happy. Uh I will just I always dream had a dream to do this. Can I take a selfie with all of you guys? Okay, just wave. I can show my wife that you know I have an important job. Okay, are you there guys? Thank you very much. Thank you. That's a first to-do list. My dream now. Okay, work. Hopefully I will not bore you to death. Uh there were a lot of subjects. Um this topic is really trending and it's really hot. I have one explanation here. So my background is data engineering, machine learning engineer. I'm sorry for all the infra guys, but no one is perfect. So data engineering, machine learning engineering, we come from another word, Hadoop word, and it's probably dead already. And we came to Kubernetes and we found a new home. Was it the perfect home? I'm not sure about this. We struggled at the beginning a lot especially that I mean Kubernetes was built for stateless. Yes. 9 years ago I mean I heard this morning that there was no way no one was thinking that Kubernetes will be the target platform for any type of workload.

And this is kind of you know I will give you like here my feedback from a from the field as a end user as a data engineer as a practitioner. Okay, so custom scheduulers there is an s it's plural but it's only two that we uh kind of managed to test and uh so far uh yeah hopefully I would not you know spend a lot of time and I just want you to go you know take take away here with two things that uh actually now we can run batch workloads which is ETL ELT and ML engineering and uh like training and serving at scale with Kubernetes like any other framework we did in the past. So the the Apache Spark case um so whatever I'm talking about Apache Spark hopefully oh sorry I need to put this uh I took already maybe two minutes okay so um whatever I'm saying about Apache Spark hopefully will apply at least for Ray who is familiar with Ray who prefers Ray to Spark okay so no really like here the the goal is to get anything that was you know to serve the purpose to work on Kubernetes. Okay. So uh this is the plan.

Hopefully I'll try to go fast and then the keep the rest for the rest. And this looks like obsolete already. I've seen in the three days I was really depressed because it's Gen AI everywhere and this was like you know oldfashioned machine learning predictive machine learning. We predict I don't know li
