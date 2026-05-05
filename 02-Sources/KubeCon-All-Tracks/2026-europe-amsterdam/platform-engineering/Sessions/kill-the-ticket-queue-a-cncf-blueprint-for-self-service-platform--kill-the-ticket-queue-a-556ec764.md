---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Bhavani Indukuri", "Aparna Prabhu", "DigitalOcean"]
sched_url: https://kccnceu2026.sched.com/event/2CW6S/kill-the-ticket-queue-a-cncf-blueprint-for-self-service-platforms-bhavani-indukuri-aparna-prabhu-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=Kill+the+Ticket+Queue%3A+A+CNCF+Blueprint+for+Self-Service+Platforms+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Kill the Ticket Queue: A CNCF Blueprint for Self-Service Platforms - Bhavani Indukuri & Aparna Prabhu, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Bhavani Indukuri, Aparna Prabhu, DigitalOcean
- Schedule: https://kccnceu2026.sched.com/event/2CW6S/kill-the-ticket-queue-a-cncf-blueprint-for-self-service-platforms-bhavani-indukuri-aparna-prabhu-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=Kill+the+Ticket+Queue%3A+A+CNCF+Blueprint+for+Self-Service+Platforms+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Kill the Ticket Queue: A CNCF Blueprint for Self-Service Platforms.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6S/kill-the-ticket-queue-a-cncf-blueprint-for-self-service-platforms-bhavani-indukuri-aparna-prabhu-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=Kill+the+Ticket+Queue%3A+A+CNCF+Blueprint+for+Self-Service+Platforms+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vrtBWPSyhr4
- YouTube title: Kill the Ticket Queue: A CNCF Blueprint for Self-Service Platfor... Bhavani Indukuri & Aparna Prabhu
- Match score: 0.872
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/kill-the-ticket-queue-a-cncf-blueprint-for-self-service-platforms/vrtBWPSyhr4.txt
- Transcript chars: 26502
- Keywords: cluster, platform, argo, events, backstage, finally, environment, actually, developer, developers, workflows, kyverno, everything, actual, clears, throat, guardrails, workflow

### Resumo baseado na transcript

We really feeling very happy to see how it's full of audience and thank you so much for you know coming this far to this room to attend this talk and we are not going to disappoint you for sure. So today we are going to talk about how we kill the ticket queue and build a self-service platform that helped us to provide a the best developer experience to our developers. So finally, after all these clarifications are done and like four teams are involved, the developers team itself and then the platform team, security team and then back to the developer team, whatever. So Kubernetes is not the problem, but the operating model is flawed and that is why it takes it takes so much of time. There were also other teams like I explained, security team, the developer team itself and you know, a lot of back and forth. For example, in our old legacy system, so those guardrails, the security review and all of that was manual.

### Excerpt da transcript

Hello everyone. We really feeling very happy to see how it's full of audience and thank you so much for you know coming this far to this room to attend this talk and we are not going to disappoint you for sure. So today we are going to talk about how we kill the ticket queue and build a self-service platform that helped us to provide a the best developer experience to our developers. So this is Bhavani Indukuri. I'm a senior software engineer two at DigitalOcean. I'm also KubeCon India 2025 co-chair and a CNCF ambassador working as as a organizer for women in CNCF. Hey hi everyone. I'm Aparna Prabhu. I'm a senior engineering manager at DigitalOcean where I manage the storage and platform teams. I've also spoken at a few CNCF events and I was a keynote speaker last year in keynote in KubeCon India. Okay, let's get started. So this is something probably many people here have I hope have experienced at some point of time. So as a back-end engineer, you have merged a new feature or in it's in you want to put it in staging, you want to test it and you need an environment.

You need a customized environment for your feature. You want to test it. So what do you do? You submit a ticket. There is in most likely there is no specialized queue for this ticket. So it joins a queue where it is competing with other like production issues, feature requests, what have you. Once it is the turn of your ticket, there is a lot of back and forth. Now people need clarifications. What kind of environment do you want? What kind of CPU limits do you want? How much memory do you need? What kind of database accesses do you need? What are your networking needs? And then there is also the security review. Here's where things like Rback, IAM, firewall rules, all these come into the picture. So as you can imagine, this back and forth takes considerable amount of time and it happens asynchronously. Okay? And quite a bit of time has elapsed from the moment the developer realized that they need an environment to this point. And mind you, we are here the actual provisioning of the environment has not even started.

So finally, after all these clarifications are done and like four teams are involved, the developers team itself and then the platform team, security team and then back to the developer team, whatever. Finally, it's time for the manual provisioning. Now the manual provisioning itself is not a very laborious process, but it is done by hand. Somebody in the platform team is stitchin
