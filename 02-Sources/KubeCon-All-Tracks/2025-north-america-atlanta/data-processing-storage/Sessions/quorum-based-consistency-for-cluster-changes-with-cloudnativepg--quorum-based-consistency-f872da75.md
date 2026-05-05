---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Data Processing + Storage"
themes: ["Storage Data", "Kubernetes Core"]
speakers: ["Jeremy Schneider", "GEICO Tech", "Gabriele Bartolini", "EDB"]
sched_url: https://kccncna2025.sched.com/event/27FfQ/quorum-based-consistency-for-cluster-changes-with-cloudnativepg-operator-jeremy-schneider-geico-tech-gabriele-bartolini-edb
youtube_search_url: https://www.youtube.com/results?search_query=Quorum-Based+Consistency+for+Cluster+Changes+With+CloudNativePG+Operator+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Quorum-Based Consistency for Cluster Changes With CloudNativePG Operator - Jeremy Schneider, GEICO Tech & Gabriele Bartolini, EDB

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Data Processing + Storage]]
- Temas: [[Storage Data]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Jeremy Schneider, GEICO Tech, Gabriele Bartolini, EDB
- Schedule: https://kccncna2025.sched.com/event/27FfQ/quorum-based-consistency-for-cluster-changes-with-cloudnativepg-operator-jeremy-schneider-geico-tech-gabriele-bartolini-edb
- Busca YouTube: https://www.youtube.com/results?search_query=Quorum-Based+Consistency+for+Cluster+Changes+With+CloudNativePG+Operator+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Quorum-Based Consistency for Cluster Changes With CloudNativePG Operator.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FfQ/quorum-based-consistency-for-cluster-changes-with-cloudnativepg-operator-jeremy-schneider-geico-tech-gabriele-bartolini-edb
- YouTube search: https://www.youtube.com/results?search_query=Quorum-Based+Consistency+for+Cluster+Changes+With+CloudNativePG+Operator+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=iQUOO3-JRK4
- YouTube title: Quorum-Based Consistency for Cluster Changes With CloudNati... Jeremy Schneider & Gabriele Bartolini
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/quorum-based-consistency-for-cluster-changes-with-cloudnativepg-operat/iQUOO3-JRK4.txt
- Transcript chars: 31506
- Keywords: postgress, replica, replication, primary, synchronous, cluster, configuration, operator, replicas, posgus, actually, database, failover, remote, important, promise, quorum, target

### Resumo baseado na transcript

But I don't want to spend too much time here because the real uh star of of this talk is actually Leonardo couldn't be here for uh family reasons. And uh he's actually the guy that has done all of the work here and we'll be talking about what he's done. So first I'm going to take a few minutes and I'm going to talk about a little bit of background of why we need this uh and at a high level the algorithm and the design and then I'm going to hand over to Gabrielli who's going to talk about kind of pop the hood open and look at how the engine was built and how it works. If we want to run Postgress on Kubernetes, one way or another, this is something that we are going to have to provide. And three of the trade-offs that we talk about the most are the ones that I've circled on here around durability, availability, and performance. But if you're going to run Postgress in cloudnative PG on Kubernetes, this is something that you should turn on.

### Excerpt da transcript

Welcome everybody. Thanks for hanging out until 3 o'clock on a Thursday. My name is Jeremy. I am a Postgress engineer at Geico. >> And my name is Gabriel Barulini. I'm VP chief architect at EDB. But I don't want to spend too much time here because the real uh star of of this talk is actually Leonardo couldn't be here for uh family reasons. And uh he's actually the guy that has done all of the work here and we'll be talking about what he's done. So uh if with this QR code you can actually see register to a webinar that we will be doing with clonerpg uh for the full uh presentation. So actually Jeremy and Leonardo will be doing this. >> Yeah. And I was going to point something out that like uh Leonardo was supposed to be giving this talk today. I'm going to back up so I don't do feedback. Um, and uh, last minute changes. We were not able to bring Leonardo with us, but we did bring his silhouette. If you look very closely at this photo that he took. You can see him in the picture. Uh, this is a whiteboard that actually has the design that we're talking about.

And it was he snapped a photo and dropped it on Slack. Uh, because that's how you build things when you have people spread all over the world trying to collaborate together on open source software. Um, one more thing, just go click the big red button. That's going to take you to the CNPG GitHub page. And I'm asking you to do that because this is really a fantastic time for you to get involved in cloudnative Postgress. There's a whole bunch of really interesting places uh that you could that you could help out and contribute and places where you could do impactful significant important stuff um and jump right in. It's yeah, there's a these were just off the top of my head about 10 areas that I thought of. Um today we're just going to be talking about one of these which is the cluster management and failover topics. So first I'm going to take a few minutes and I'm going to talk about a little bit of background of why we need this uh and at a high level the algorithm and the design and then I'm going to hand over to Gabrielli who's going to talk about kind of pop the hood open and look at how the engine was built and how it works.

All right to set uh to sort of like set the stage for for going through this today. There are kind of just two things I want to I want to briefly touch on. Uh the first thing is that Postgress itself the Postgress engine provides core replication capabilities. So Postgress can r
