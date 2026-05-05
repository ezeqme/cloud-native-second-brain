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
themes: ["AI ML", "Security", "Networking", "Community Governance"]
speakers: ["Huabing (Robin) Zhao", "Tetrate"]
sched_url: https://kccnceu2025.sched.com/event/1tczX/securing-the-gateway-a-deep-dive-into-envoy-gateways-advanced-security-policy-huabing-robin-zhao-tetrate
youtube_search_url: https://www.youtube.com/results?search_query=Securing+the+Gateway%3A+A+Deep+Dive+Into+Envoy+Gateway%27s+Advanced+Security+Policy+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Securing the Gateway: A Deep Dive Into Envoy Gateway's Advanced Security Policy - Huabing (Robin) Zhao, Tetrate

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Networking]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Huabing (Robin) Zhao, Tetrate
- Schedule: https://kccnceu2025.sched.com/event/1tczX/securing-the-gateway-a-deep-dive-into-envoy-gateways-advanced-security-policy-huabing-robin-zhao-tetrate
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+the+Gateway%3A+A+Deep+Dive+Into+Envoy+Gateway%27s+Advanced+Security+Policy+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Securing the Gateway: A Deep Dive Into Envoy Gateway's Advanced Security Policy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tczX/securing-the-gateway-a-deep-dive-into-envoy-gateways-advanced-security-policy-huabing-robin-zhao-tetrate
- YouTube search: https://www.youtube.com/results?search_query=Securing+the+Gateway%3A+A+Deep+Dive+Into+Envoy+Gateway%27s+Advanced+Security+Policy+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=x8wEo6ZDT1g
- YouTube title: Securing the Gateway: A Deep Dive Into Envoy Gateway's Advanced Security Pol... Huabing (Robin) Zhao
- Match score: 0.962
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/securing-the-gateway-a-deep-dive-into-envoy-gateways-advanced-security/x8wEo6ZDT1g.txt
- Transcript chars: 14188
- Keywords: gateway, policy, security, define, traffic, authentication, secret, access, amazon, provider, request, another, control, authorization, simple, application, identity, information

### Resumo baseado na transcript

I'm a maternal gateway project and also I contribute to way and also have another heart. So although this might not be the flash topic like generic AIM is a bored no security stuff where or old but I think we can all agree that security gateway traffic is super super important for any of your application. way to man to manage and handle the gateway traffic for you and Today our focus is security policy security. your own feature but without necessarily modifying those core resources directly though that's a very powerful very flexible way to extend how how the G API standard works and that's exactly how security policy works So you just defy your security policy. fourth level gateway level which means you can define one security policy and applies it to the gateway level and all the routes under that gateway will get protected so you don't worry about it you can also define another security policy for example you may have a have endpoint which is uh very sensitive can only be accessed by administrator so you can define another security policy and apply applied to that specific route to over to override the global one.

### Excerpt da transcript

Let's get started. Hey, London. Super excited to be here. So, uh, a little bit of myself. I'm No, and I wear two hearts. My open source heart. I'm a maternal gateway project and also I contribute to way and also have another heart. This one my company. Okay. I'll just wear this one. So although this might not be the flash topic like generic AIM is a bored no security stuff where or old but I think we can all agree that security gateway traffic is super super important for any of your application. So it's definitely something worth talking about. Today we are going to dive into some advanced security policies for gateway. I will also give you a quick demo on how you can use it for OID authentication and authorization. Okay, let's jump in. First, I saw some friends from our community. So, I'd like to do a quick poll. How many of you have used or played with Gway on your laptop or maybe testing? Can you show me your hands? Oh, thank you. A bunch of them. Are there anyone already put it into in production? Anyone?

Okay, I say one, two, one, two, three. Oh, awesome. Awesome. love to say that. So if you are a lot of very familiar with onway gateway is just a control plan to make it much much easier for you to run only proxy as an API gateway. That's it. That's it. We know how hard it can be if you like uh uh runway proxy by manually configure them. It's like a ton of thousands of y file. It's a disaster. But instead of manually configuring in way our gateway just use the kubber gateway API uh to help you set up and configure the proxy automatically whether it's a standalone service or inside of kubernetes so without all the hassle so basically is a simple way to man to manage and handle the gateway traffic for you and Today our focus is security policy security. So what's exactly is that or more broadly what do we mean by a policy right so we mentioned that only getway uses corated gateway API which is a standard and only gateway is one of the implementation so that's it and one of the coolest thing I love about the G API it's uh is the the idea of polish attachment basically you can define your own traffic policy and uh attach them to the core gateway API resources like gateway HP route to enhance its capability to add your own feature but without necessarily modifying those core resources directly though that's a very powerful very flexible way to extend how how the G API standard works and that's exactly how security policy works So you just defy your securi
