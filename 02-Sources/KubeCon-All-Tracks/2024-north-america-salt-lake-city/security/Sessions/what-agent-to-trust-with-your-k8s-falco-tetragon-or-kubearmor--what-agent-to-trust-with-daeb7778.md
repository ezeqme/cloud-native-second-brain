---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Security"
themes: ["AI ML", "Security"]
speakers: ["Henrik Rexed", "Dynatrace"]
sched_url: https://kccncna2024.sched.com/event/1i7rE/what-agent-to-trust-with-your-k8s-falco-tetragon-or-kubearmor-henrik-rexed-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=What+Agent+to+Trust+with+Your+K8s%3A+Falco%2C+Tetragon+or+KubeArmor%3F+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What Agent to Trust with Your K8s: Falco, Tetragon or KubeArmor? - Henrik Rexed, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Security]]
- Temas: [[AI ML]], [[Security]]
- País/cidade: United States / Salt Lake City
- Speakers: Henrik Rexed, Dynatrace
- Schedule: https://kccncna2024.sched.com/event/1i7rE/what-agent-to-trust-with-your-k8s-falco-tetragon-or-kubearmor-henrik-rexed-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=What+Agent+to+Trust+with+Your+K8s%3A+Falco%2C+Tetragon+or+KubeArmor%3F+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What Agent to Trust with Your K8s: Falco, Tetragon or KubeArmor?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7rE/what-agent-to-trust-with-your-k8s-falco-tetragon-or-kubearmor-henrik-rexed-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=What+Agent+to+Trust+with+Your+K8s%3A+Falco%2C+Tetragon+or+KubeArmor%3F+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=obRMpKsjYPc
- YouTube title: What agent to trust with your k8s: Falco, Tetragon or KubeAmor?
- Match score: 1.072
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/what-agent-to-trust-with-your-k8s-falco-tetragon-or-kubearmor/obRMpKsjYPc.txt
- Transcript chars: 43598
- Keywords: basically, events, security, kernel, tetragonon, cubecape, policies, actual, produce, everything, process, cluster, actually, course, ebpf, server, figure, deploy

### Resumo baseado na transcript

I think looking at your faces, you definitely look fresher than before. This is due to the fact that, as I mentioned in the keynote or before the keynote, we actually had to drop in some people because many speakers actually quit on us. uh I think low the performance engineing practice is a fantastic practice to learn architecture because you discover different architecture patterns you know how to tweak them to tune them I think it's the best way of becoming architecture for the future so for those who never been in performance engineering and you want to discover new technologies and new stuff go ahead it's the perfect practice for that so I used I mean I'm still in fact part of a podcast team called perf bites that's why performance is still in my heart And you'll see that the way I'm designing that talk is about performance. It used to be a podcast now we are YouTube channel that uh talks about only a performance stuff uh performance methodology and stuff like this.

### Excerpt da transcript

All right, welcome everybody. Welcome back in hall six here. I hope you all had a good cup of coffee or two. I think looking at your faces, you definitely look fresher than before. Our next speaker, he's actually coming here all the way from Ma. And as you might recognize, he's also one of our co-organizers. This is due to the fact that, as I mentioned in the keynote or before the keynote, we actually had to drop in some people because many speakers actually quit on us. Ex exactly 13 speakers quit on us out of 32 which is more than a third. So that's why we had Henrik as a drop in but he's a really really really good speaker. He's a podcast host. Anybody know is it observable. Yes, some hands over there. The other guys definitely check it out. He's an avid YouTube producer. He has really high quality content. He also did content on his next talk. This talk is actually going to be focused on Kubernetes security and which tool to trust with. Henrik is a senior staff engineer at Dino Trace. I think that's pretty much the best you can get.

Correct me if I'm wrong. >> I don't know. SK is the limit. Please give him a hand and enjoy the next 45 minutes. [Applause] Thanks for the intro. Um, all right. So, I hope you like security. Who likes security here in the hands? I don't. Yeah, a couple of hands here. Uh, how many of you are doing any runtime security? Do you know any runtime agent? Ah, a couple of hands. Okay. All right. So, today we are going into an adventure together. So, if you're up to that, I need your help because I don't like to present uh 45 minutes slides. It's kind of boring. So, I need your support. So, are you ready to follow this adventure? >> That's a small Yeah. So because we take a five minutes break, grab some more coffee and come back and then I will re ask the question. All right. If you So are you ready for the adventure? >> Well, a bit better. All right. So we it's going to be uh if you recognize an advent Avenger theme. So we're going to have couple of security superheroes and we're going to figure out which one is the actual Avenger.

So that's the purpose of this talk. Before I uh start uh this presentation, let me just do a few more words about myself even if you did a great job. Uh so I am a CNF ambassador. Uh it's for now a year and a half now. Uh and also um I spent all my career as a performance engineer. So meaning testing, braking, tuning. uh I think low the performance engineing practice is a fantastic practice to learn arch
