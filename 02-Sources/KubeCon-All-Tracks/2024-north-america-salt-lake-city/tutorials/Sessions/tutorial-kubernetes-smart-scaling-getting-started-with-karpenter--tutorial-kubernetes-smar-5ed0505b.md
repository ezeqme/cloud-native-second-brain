---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Tutorials"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Changsu Lee", "Raj Saha", "AWS", "Wilson Darko", "Charlie McBride", "Microsoft", "Praseeda Sathaye", "Amazon"]
sched_url: https://kccncna2024.sched.com/event/1i7n3/tutorial-kubernetes-smart-scaling-getting-started-with-karpenter-changsu-lee-raj-saha-aws-wilson-darko-charlie-mcbride-microsoft-praseeda-sathaye-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Tutorial%3A+Kubernetes+Smart+Scaling%3A+Getting+Started+with+Karpenter+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Tutorial: Kubernetes Smart Scaling: Getting Started with Karpenter - Changsu Lee & Raj Saha, AWS; Wilson Darko & Charlie McBride, Microsoft; Praseeda Sathaye, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Tutorials]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: United States / Salt Lake City
- Speakers: Changsu Lee, Raj Saha, AWS, Wilson Darko, Charlie McBride, Microsoft, Praseeda Sathaye, Amazon
- Schedule: https://kccncna2024.sched.com/event/1i7n3/tutorial-kubernetes-smart-scaling-getting-started-with-karpenter-changsu-lee-raj-saha-aws-wilson-darko-charlie-mcbride-microsoft-praseeda-sathaye-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Tutorial%3A+Kubernetes+Smart+Scaling%3A+Getting+Started+with+Karpenter+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Tutorial: Kubernetes Smart Scaling: Getting Started with Karpenter.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7n3/tutorial-kubernetes-smart-scaling-getting-started-with-karpenter-changsu-lee-raj-saha-aws-wilson-darko-charlie-mcbride-microsoft-praseeda-sathaye-amazon
- YouTube search: https://www.youtube.com/results?search_query=Tutorial%3A+Kubernetes+Smart+Scaling%3A+Getting+Started+with+Karpenter+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=3v7Srpx1HVc
- YouTube title: Tutorial: Kubernetes Smart Scaling: Getting Started with Karpenter - Panel
- Match score: 1.035
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/tutorial-kubernetes-smart-scaling-getting-started-with-karpenter/3v7Srpx1HVc.txt
- Transcript chars: 24863
- Keywords: carpenter, follow, environment, workshop, disruption, cluster, actually, workload, instance, instances, account, please, instructions, consolidation, console, cost, within, essentially

### Resumo baseado na transcript

are here for the smart scaling with Carpenter and we'll tell you why Carpenter is so smart in this session uh so let me start and I think uh you already went through this uh but we have this up on the cubec con uh website so you can take a look at that as well so my name is prida and I am um principal container specialist and also open source specialist at AWS I have uh my colleagues and my friends over here uh who will be my

### Excerpt da transcript

are here for the smart scaling with Carpenter and we'll tell you why Carpenter is so smart in this session uh so let me start and I think uh you already went through this uh but we have this up on the cubec con uh website so you can take a look at that as well so my name is prida and I am um principal container specialist and also open source specialist at AWS I have uh my colleagues and my friends over here uh who will be my uh co-s speakers they will introduce themselves so today we are going to talk about Carpenter yay okay first uh raise your hands who are actually using cluster Auto skill today cluster Autos Skiller yes so I I'm assuming that you are here to learn that why I should move to Carpenter right yeah then you are in the right session and raise your hands who are already trying Carpenter awesome awesome okay you'll learn more okay so uh before diving into Carpenter I would like to talk about what are the challenges right why we need Carpenter so if you see cluster Autos Skiller and Carpenter both are kubernetes Auto scalers right uh and they work exactly the similar way but what are the current challenges what users and customers are facing today so with cluster autoscaler uh it has to be associated with the autoscaling groups so you have no Group which are associated to autoscaling groups and those can only be configured with one instance type right and you before you start about uh deploying or your workload you need to make sure that you create those node groups with that certain instance type right but what about like another team needs another type of workload here like you can see GPU workload and it needs a different type of GPU instances right so in that case uh currently in cluster autoscaler uh you have to basically create another node group and then it will create another autoscaling group for that right and then that workload will uh be deployed into that node group correct so Carpenter actually removes completely the concept of node group and autoscaling group basically uh it works with one uh uh declarative configuration you can actually mention what workloads you want to deploy and it is smart enough to actually uh spin up the instance for your workload depending upon what resources you have in your Port spec so what we are see you can see now the GPU workload is going to this uh instance p4d instance and that's what we talk about Carpenter that it provides uh its Provisions appropriate instances based on your ports pack right
