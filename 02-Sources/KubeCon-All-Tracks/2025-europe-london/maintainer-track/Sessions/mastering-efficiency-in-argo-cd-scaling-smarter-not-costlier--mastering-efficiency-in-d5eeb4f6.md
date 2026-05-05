---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "GitOps Delivery", "SRE Reliability", "Community Governance"]
speakers: ["Alexander Matyushentsev", "Akuity"]
sched_url: https://kccnceu2025.sched.com/event/1tcxq/mastering-efficiency-in-argo-cd-scaling-smarter-not-costlier-alexander-matyushentsev-akuity
youtube_search_url: https://www.youtube.com/results?search_query=Mastering+Efficiency+in+Argo+CD%3A+Scaling+Smarter%2C+Not+Costlier+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Mastering Efficiency in Argo CD: Scaling Smarter, Not Costlier - Alexander Matyushentsev, Akuity

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[GitOps Delivery]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Alexander Matyushentsev, Akuity
- Schedule: https://kccnceu2025.sched.com/event/1tcxq/mastering-efficiency-in-argo-cd-scaling-smarter-not-costlier-alexander-matyushentsev-akuity
- Busca YouTube: https://www.youtube.com/results?search_query=Mastering+Efficiency+in+Argo+CD%3A+Scaling+Smarter%2C+Not+Costlier+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Mastering Efficiency in Argo CD: Scaling Smarter, Not Costlier.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxq/mastering-efficiency-in-argo-cd-scaling-smarter-not-costlier-alexander-matyushentsev-akuity
- YouTube search: https://www.youtube.com/results?search_query=Mastering+Efficiency+in+Argo+CD%3A+Scaling+Smarter%2C+Not+Costlier+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bpsclYlGl2s
- YouTube title: Mastering Efficiency in Argo CD: Scaling Smarter, Not Costlier - Alexander Matyushentsev, Akuity
- Match score: 0.875
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/mastering-efficiency-in-argo-cd-scaling-smarter-not-costlier/bpsclYlGl2s.txt
- Transcript chars: 23119
- Keywords: argo, application, cost, cluster, traffic, server, applications, controller, multiple, control, resources, single, basically, clusters, several, reason, reduce, manage

### Resumo baseado na transcript

So uh title is mastering efficiency in Argo CD and uh we will be talking about how to what does it take to scale Argo CD and how much does it cost and I will share with you you know tips how to reduce your cloud bill. And I'm also co-founder of company called Acuity where we run Argo CD for other companies. And so uh generally Argo CD won't cost you anything because highly likely it will just land on some nodes inside of your cluster that have spare memory and CPU and Argo will apply a little bit of pressure on Kubernetes API server of your cluster but it's really hard to translate it to money. one is stateful set and a J proxy that balance requests and you might end up having multiple controllers if you manage multiple clusters and this transition also requires uh infrastructure that would cost you some money. And so last but not least, um you are going to have to pay for traffic and it's kind of not obvious because if you use AWS, those costs will be hidden under this shy EC2 other section and but it surprisingly big like in in multiple cases this network cost is around 30% of the bill. So it is significant and as I will share a little later sometimes it actually can spike and there is but there is way to mitigate the close cost close spike.

### Excerpt da transcript

All right, we have 30 minutes only. So I want to start the presentation one more time. Welcome everyone uh to presentation. So uh title is mastering efficiency in Argo CD and uh we will be talking about how to what does it take to scale Argo CD and how much does it cost and I will share with you you know tips how to reduce your cloud bill. Uh before I start, quick introduction. So my name is uh Alexander Matensv. Don't try to pronounce my last name. Uh so I'm one of the Argo project co-creators. I've been working on this project for like seven or eight years. And I'm also co-founder of company called Acuity where we run Argo CD for other companies. And in the last several years, we learned several lessons uh about uh how much money we have to spend to run Argo CD at scale. And I'm going to share this learnings with you and hopefully help you to save some money for your organization. Um here is today's agenda. It's kind of simple. First, I want to basically convince you that this topic was a conversation.

So we all know that if you use Argo CD you know it's cheap and very efficient and until you have to run it at a really large scale and so uh it can get expensive at some point and I want to share with you some numbers of what expensive really means so you can decide if it's time for you to invest you know uh some effort into reducing the build and optimizing and I'm going to share with you some lessons we've learned and solutions that you can apply to reduce cost of your Argo CD. Um, and now it's time to start. Um, so I do want to start from the statement that Argo CD is, you know, it's not going to cost you a lot from the beginning. So one of the most common ways to run Argo CD is to install it into the cluster that you plan to manage. And uh, this is the screenshot of freshly installed Argo CD on a small cluster. And as you can see, we have quite a lot of pods, but combined they use a fraction of CPU and maybe 100 megabytes of memory. Couple of those pods are even optional, such as DEX and notifications controller.

You can don't even run them if you don't need to. And uh there is a diagram that shows how those components interact. And as you can see, there's basically four of them that you would need to install and pay for. And so uh generally Argo CD won't cost you anything because highly likely it will just land on some nodes inside of your cluster that have spare memory and CPU and Argo will apply a little bit of pressure on Kubernetes API server of
