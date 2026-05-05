---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["Max Körbächer", "Liquid Reply", "Alexa Griffith", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1tx7K/the-explorers-guide-to-cloud-native-genai-platform-engineering-max-korbacher-liquid-reply-alexa-griffith-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=The+Explorer%27s+Guide+To+Cloud+Native+GenAI+Platform+Engineering+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Explorer's Guide To Cloud Native GenAI Platform Engineering - Max Körbächer, Liquid Reply & Alexa Griffith, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Max Körbächer, Liquid Reply, Alexa Griffith, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1tx7K/the-explorers-guide-to-cloud-native-genai-platform-engineering-max-korbacher-liquid-reply-alexa-griffith-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=The+Explorer%27s+Guide+To+Cloud+Native+GenAI+Platform+Engineering+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Explorer's Guide To Cloud Native GenAI Platform Engineering.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7K/the-explorers-guide-to-cloud-native-genai-platform-engineering-max-korbacher-liquid-reply-alexa-griffith-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=The+Explorer%27s+Guide+To+Cloud+Native+GenAI+Platform+Engineering+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8ta_zFiUG1s
- YouTube title: The Explorer's Guide To Cloud Native GenAI Platform Engineering - Max Körbächer & Alexa Griffith
- Match score: 0.89
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-explorers-guide-to-cloud-native-genai-platform-engineering/8ta_zFiUG1s.txt
- Transcript chars: 26903
- Keywords: platform, inference, models, gateway, little, source, running, caching, provide, envoy, actually, engineering, question, around, backstage, features, already, performance

### Resumo baseado na transcript

I'm a senior software engineer at Bloomberg working on their AI platforms and uh today we will have a little exploratory journey throughout the platform engineering genai universe. Our idea behind is like either you pick up little items out of this whole universe or you see a full-blown large platform but you never see the journey in between and how you maybe come from one thing to the other thing and that's how our journey will start for also today. So, Kubernetes platform engineering needs to bring in some kind of flexibility of allow us to adopt to all of this very fast changes with this very fast explosions on the market and maybe also roll out some of the uh market player which we can see and Kubernetes is therefore the perfect platform because it knows already from 2020 some of the automation hype then we go to edge IoT telco last year and always about internal development platforms and stuff like that. But the reason for it is not just because it's a hype but we provide with Kubernetes and platform engineering actually a very good foundation to drive this kind of innovation and provide also an environment to frequently change some of the tools which maybe So, actually to prevent that the demon gods uh screw up this talk, we thought like we are smart and pre-record something.

### Excerpt da transcript

Hi everyone and welcome to our talk. My name is Max Kerbesha and my name is Alexa Griffith. I'm a senior software engineer at Bloomberg working on their AI platforms and uh today we will have a little exploratory journey throughout the platform engineering genai universe. Our idea behind is like either you pick up little items out of this whole universe or you see a full-blown large platform but you never see the journey in between and how you maybe come from one thing to the other thing and that's how our journey will start for also today. We would like to go step by step through some little ideas. We'll get you set up and then we'll dive into one to other demos, show you a few little things and uh yeah, we'll round it up in the end. Sounds good. So this map you maybe know and usually you know this way more bigger landscape from the cloudnative computing foundation but this is a specialized map just showing the AI landscape from Kubernetes and the CNCF universe. The very interesting thing is it's actually kind of small.

So AI happens with cloud native, but it also happens alongside of the cloud native universe. What I mean with this is like this beautiful map and that's actually insane and it's old 2023. Um, but it's also great because you can see different blocks in it. You see infrastructure, you see data analytics, you see also the open source layer which is like on the bottom this uh kind of greenish um area. Now, keep your eyes on it. Don't blink because there will be a little change between 2023 and 2024. It's almost feels like it's exploded, right? I'm still waiting for the 2025 version. I would love to bring it here, but I believe there's so much changes on the market that the guys have built this map need a little bit more time. But why this map is now relevant to us is that we need to understand we live in a cloudnative ecos and everything is moving fast. We have a lot of open source projects, a lot of things going on, but we very often talk about the same things where yes, you find also a lot of commercial solutions for sure, but it also means there's a total other entire echosace that we maybe haven't thought of yet or maybe have already provided solutions, right?

So, Kubernetes platform engineering needs to bring in some kind of flexibility of allow us to adopt to all of this very fast changes with this very fast explosions on the market and maybe also roll out some of the uh market player which we can see and Kubernetes is therefore the pe
