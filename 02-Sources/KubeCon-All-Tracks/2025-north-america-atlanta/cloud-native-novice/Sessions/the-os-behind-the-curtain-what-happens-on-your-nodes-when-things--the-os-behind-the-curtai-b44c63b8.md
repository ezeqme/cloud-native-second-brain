---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Cloud Native Novice"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Joe Thompson", "Clarity Business Solutions"]
sched_url: https://kccncna2025.sched.com/event/27FZB/the-os-behind-the-curtain-what-happens-on-your-nodes-when-things-happen-in-your-cluster-joe-thompson-clarity-business-solutions
youtube_search_url: https://www.youtube.com/results?search_query=The+OS+Behind+the+Curtain%3A+What+Happens+on+Your+Nodes+When+Things+Happen+in+Your+Cluster+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The OS Behind the Curtain: What Happens on Your Nodes When Things Happen in Your Cluster - Joe Thompson, Clarity Business Solutions

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United States / Atlanta
- Speakers: Joe Thompson, Clarity Business Solutions
- Schedule: https://kccncna2025.sched.com/event/27FZB/the-os-behind-the-curtain-what-happens-on-your-nodes-when-things-happen-in-your-cluster-joe-thompson-clarity-business-solutions
- Busca YouTube: https://www.youtube.com/results?search_query=The+OS+Behind+the+Curtain%3A+What+Happens+on+Your+Nodes+When+Things+Happen+in+Your+Cluster+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The OS Behind the Curtain: What Happens on Your Nodes When Things Happen in Your Cluster.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZB/the-os-behind-the-curtain-what-happens-on-your-nodes-when-things-happen-in-your-cluster-joe-thompson-clarity-business-solutions
- YouTube search: https://www.youtube.com/results?search_query=The+OS+Behind+the+Curtain%3A+What+Happens+on+Your+Nodes+When+Things+Happen+in+Your+Cluster+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=9KCXvQU10yY
- YouTube title: The OS Behind the Curtain: What Happens on Your Nodes When Things Happen in Your Clu... Joe Thompson
- Match score: 0.998
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-os-behind-the-curtain-what-happens-on-your-nodes-when-things-happe/9KCXvQU10yY.txt
- Transcript chars: 28209
- Keywords: actually, container, tables, little, around, overlay, mounts, anybody, cluster, containers, croups, mounted, slides, usually, kernel, systems, memory, default

### Resumo baseado na transcript

Now, they shortened the they shortened the sessions by about five minutes this year compared to previous years. So, I'm going to fly a little bit so I can leave plenty of time for questions and and maybe some demo if we can squeeze it in if the network cooperates. Now, the other thing is we're going to be talking about some low-level Linux features that power Kubernetes, but they aren't Kubernetes per se. Now of the people who've ever heard of control groups, how many of you know it only from taking the Red Hat performance tuning exam? So, these are all the very basic basic things that kind of go into what makes Kubernetes actually work on a Linux node. Now, what we're going to cover is basically how Linux puts your Kubernetes workloads into a box.

### Excerpt da transcript

Well, let's talk about why I'm here. Why are we all here? I assume some of you came here to learn something. So, a little bit about me. Now, they shortened the they shortened the sessions by about five minutes this year compared to previous years. So, I'm going to fly a little bit so I can leave plenty of time for questions and and maybe some demo if we can squeeze it in if the network cooperates. But, I am Joe Thompson. You may remember me from some of my previous talks at CubeCon, like please stop writing operators. We have enough. We don't need any. No, we actually do need some more. But I did that talk and it gets passed around occasionally. Um the other one that I did at scale because I've actually come to believe this is we need to destroy web PKI in order to save it. It's currently not working. I have links to those talks. I'm not going to belabor those points here. I've been in it for about 30 years. the last decade or so have been mostly focused on Kubernetes. I have a list of previous employers there and I currently work with a company called Clarity Business Solutions.

You've probably never heard of it. We are a very small company based out of Lentham, Maryland. And uh they just recently I was a consulting engineer when I started there. They just recently changed my title to cloudnative architect. Gave me fancy business cards, the whole deal. And there's some contact info on the right. Now, don't worry. You can take a picture of this slide if you want. Don't worry because at the end there's going to be a QR code and a tiny URL link that can go to the live slides on the web and you'll be able to click all these links and copy and paste things and all manner of wonderful stuff. So, I always like to take the temperature of the audience a little bit when I start these. Uh, who's at their first CubeCon? Hands up. Quite a lot. Yeah, it's usually 2/3 of the room. Uh, who here has been to CubeCon before? Okay. Who's been working with Kubernetes more than a year? All right. More than five years. Okay. More than 15 years. Uh, see. Okay. Sometimes I catch a couple liars in the room that way.

If this is your first CubeCon, you may already know this from getting dehydrated yesterday. Drink more water. I have my water bottle here. If you don't have a water bottle, go to the CNCF store. They have these wonderful little water bottles there with logos on them and everything. Get one. Use the bottle filler fountains. Keep that thing filled through the day. If y
