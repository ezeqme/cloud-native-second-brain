---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Cloud Native Novice"
themes: ["Security", "Kubernetes Core"]
speakers: ["Bruno Gabriel da Silva", "Sysdig", "Henrique Santana", "AWS"]
sched_url: https://kccnceu2025.sched.com/event/1txGT/surviving-day2-picking-the-right-tool-to-secure-your-kubernetes-habitat-bruno-gabriel-da-silva-sysdig-henrique-santana-aws
youtube_search_url: https://www.youtube.com/results?search_query=Surviving+Day2+%3A+Picking+the+Right+Tool+To+Secure+Your+Kubernetes+Habitat+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Surviving Day2 : Picking the Right Tool To Secure Your Kubernetes Habitat - Bruno Gabriel da Silva, Sysdig & Henrique Santana, AWS

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Bruno Gabriel da Silva, Sysdig, Henrique Santana, AWS
- Schedule: https://kccnceu2025.sched.com/event/1txGT/surviving-day2-picking-the-right-tool-to-secure-your-kubernetes-habitat-bruno-gabriel-da-silva-sysdig-henrique-santana-aws
- Busca YouTube: https://www.youtube.com/results?search_query=Surviving+Day2+%3A+Picking+the+Right+Tool+To+Secure+Your+Kubernetes+Habitat+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Surviving Day2 : Picking the Right Tool To Secure Your Kubernetes Habitat.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txGT/surviving-day2-picking-the-right-tool-to-secure-your-kubernetes-habitat-bruno-gabriel-da-silva-sysdig-henrique-santana-aws
- YouTube search: https://www.youtube.com/results?search_query=Surviving+Day2+%3A+Picking+the+Right+Tool+To+Secure+Your+Kubernetes+Habitat+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=FqUPqroF-Rw
- YouTube title: Surviving Day2 : Picking the Right Tool To Secure Your... Bruno Gabriel da Silva & Henrique Santana
- Match score: 0.841
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/surviving-day2-picking-the-right-tool-to-secure-your-kubernetes-habita/FqUPqroF-Rw.txt
- Transcript chars: 22808
- Keywords: secrets, container, external, basically, inside, specific, security, runtime, layers, application, running, kernel, projects, directly, change, resource, forest, provide

### Resumo baseado na transcript

Before we start, I'd like to do a quick question for you, make a quick question for you about do you know how many CNCF projects, security projects exist today? Before you provide the answer, hold on, let me provide some an image that will help you to to make the the math from your side. So, GitHub uh stars or blog post or even you know uh cubernetes uh cubecon talks and based on those we kind like okay how can we structure this in a way that I can understand the flux or the flow where the security tools fits in the security space as also the idea here is get a little bit of oneonone idea of how the secure around kubernetes can be used for those who decide to get four kind of stages build, deploy, start, and run. When I teach in my company, especially when I talk to people that starting the security journey, I like to compare this when like you do a recipe of a cake. Very similar in the container or Kubernetes world, we just download packages or use you know sources that maybe are not so trustable or we don't have the uh knowledge or time to inspect them.

### Excerpt da transcript

Thank you so much for being here. I know it's Friday, the last day. I hope so far you had a great event so far. And once again, thanks. Thank you so much for being here. Before we start, I'd like to do a quick question for you, make a quick question for you about do you know how many CNCF projects, security projects exist today? I'll give some hints, some options to you to think about it. So between these options, what do you think? Before you provide the answer, hold on, let me provide some an image that will help you to to make the the math from your side. So this image is about all the secure CNCF opensource projects. So now it's easy to know the option, right? So let's check who thinks that the they the answer is letter E. A sorry no one. Okay. One there B. Okay. A lot of people. What about C? Okay. I think B is the winner. So the letter C and to be more precisely it's 80 and counting it's growing fast. It's not easy from the image to get this number. You need to count because the the squares are not the same size.

My name is Hickantana. I'm principal cloud support engineer at AWS. I work with uh customers for ECS and EKS for about five years almost six year now. I'm based in Dublin. I'm Brazilian and together with me it's Hello, I am Bruno Silva, senior solutions engineer at CYIC. I'm also Brazilian live in Dublin. A little bit about myself uh before knowing this Kubernetes thing. I work a lot with no corporate leash legacy let's say technology like Microsoft products and since then I discovered this open source and world I shift to this and welcome to surviving the two picking the right tool to secure your cubernetes habitat. So if you read uh the description of all your talk you may be thinking how can we correlate technology and you know open source tools. Well, I hope our presentation uh make this a little bit clear. So, starting with, you know, the animal kingdom, we have some animals that are very similar even in size, in shape, but they're not the same. Let's get, for example, like a tiger and a lion, but they overlap in some things, you know, kind of the family, etc., but they have some social ways to do or different strategies to hunt.

And this is where I think the tools in open source space as we saw 80 at least well when the slides maybe a new one was announced during cubecom and this is how we want to get this uh clarify in this talk. We don't have time of course to cover all the 80 tools otherwise well it's going to take a long time and
