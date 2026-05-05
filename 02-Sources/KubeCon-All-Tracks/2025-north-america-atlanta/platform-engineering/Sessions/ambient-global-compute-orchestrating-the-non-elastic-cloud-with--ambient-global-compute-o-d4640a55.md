---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Jago Macleod", "Google"]
sched_url: https://kccncna2025.sched.com/event/27FZZ/ambient-global-compute-orchestrating-the-non-elastic-cloud-with-kubernetes-jago-macleod-google
youtube_search_url: https://www.youtube.com/results?search_query=Ambient+Global+Compute%3A+Orchestrating+the+Non-Elastic+Cloud+With+Kubernetes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Ambient Global Compute: Orchestrating the Non-Elastic Cloud With Kubernetes - Jago Macleod, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Jago Macleod, Google
- Schedule: https://kccncna2025.sched.com/event/27FZZ/ambient-global-compute-orchestrating-the-non-elastic-cloud-with-kubernetes-jago-macleod-google
- Busca YouTube: https://www.youtube.com/results?search_query=Ambient+Global+Compute%3A+Orchestrating+the+Non-Elastic+Cloud+With+Kubernetes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Ambient Global Compute: Orchestrating the Non-Elastic Cloud With Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZZ/ambient-global-compute-orchestrating-the-non-elastic-cloud-with-kubernetes-jago-macleod-google
- YouTube search: https://www.youtube.com/results?search_query=Ambient+Global+Compute%3A+Orchestrating+the+Non-Elastic+Cloud+With+Kubernetes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=r-UBNuWkUG8
- YouTube title: Ambient Global Compute: Orchestrating the Non-Elastic Cloud With Kubernetes - Jago Macleod, Google
- Match score: 0.961
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/ambient-global-compute-orchestrating-the-non-elastic-cloud-with-kubern/r-UBNuWkUG8.txt
- Transcript chars: 22306
- Keywords: capacity, workload, cluster, running, pretty, machine, machines, actually, region, instances, instead, another, multiple, reserved, discounts, sometimes, little, gpu

### Resumo baseado na transcript

Hi everybody, my name is JGO Mloud uh and we are going to talk about an interesting and emerging aspect of the public cloud especially uh and uh I'm super excited that the right direction. Okay, so the cloud has basically come full circle and it's an really interesting moment. Um but it's pretty great from efficiency perspective and power management and it's a wonderful architecture, but you do have to compile your application into multiple architectures and there's complexity. So we have this constrained capacity and the kind of big idea that I want to leave you with is instead of scaling infinitely horizontally you kind of scale vertically in time and you think about the priority of the workloads that you're running as a ongoing ever growing queue. uh you know high discounts uh but you used to try and pay the least for what you need right now and you run everything right now because it's infinite capacity no one has to wait ever you just scale horizontally uh and instead it's It's pretty hard with what's available in upstream open source Kubernetes.

### Excerpt da transcript

Hi everybody, my name is JGO Mloud uh and we are going to talk about an interesting and emerging aspect of the public cloud especially uh and uh I'm super excited that the right direction. Okay, so the cloud has basically come full circle and it's an really interesting moment. There was this beautiful vision of the cloud. It was this magical endpoint in the sky. You would just call it. It would provision things. You never had to know about any of the underlying infrastructure. You just pay for what you want. Uh and so we started out many years ago and it was data centers, right? It was all about data centers. You would rack and stack and you had to think months and months in advance and buy things and they get shipped. There's that beautiful smell when you unbox a machine and you breathe in that air as it's offging and you get to plug it in and rack and stack it and you get really like finicky about how you laid out your cables. We all took great pride in that, right? Uh but it was really challenging.

You had to think months, years in advance for capacity planning. Uh, and when someone on your team, one of your teams wanted more capacity, they had to let you know. You had to put it in this big spreadsheet. They would think, "Oh, you know, I made games at Disney for a while." And they would say, "It's going to be the next Candy Crush. We need a million machines." And you'd kind of, do we, though? Uh, and so you had this sort of like mental linear regression analysis about the optimism of your product teams and how much you would really need. And then you had this portfolio view. Uh and then we sort of moved along uh and we got to this elastic cloud that was super awesome, right? We went through VMs. You could provision a VM in minutes, hours maybe, uh instead of months. Uh and then you go into the cloud and you like you don't even have to think about the machines and finally we get to now. And now we've sort of come full circle. And here's why. Uh well there back going back to the very beginning we would overprovision.

You were like okay I know you're not going to do exactly what you say product team but I also know that I don't want to get in trouble if you do. So we would buy more machines. We'd plug them in and then everything's running at 15% utilization. You're like way overprovisioned and Black Friday's coming so the rest of the year you run at 3%. And so VMs made this much much better. we could spread VMs across. There was like OpenStack and what w
