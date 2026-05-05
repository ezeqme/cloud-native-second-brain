---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "AI + ML"
themes: ["AI ML", "Community Governance"]
speakers: ["Bahaulddin Shammary", "Dell", "Andrey Shorov", "Ericsson"]
sched_url: https://kccnceu2026.sched.com/event/2CW0b/securing-the-aiml-lifecycle-with-mlsecops-open-source-best-practices-bahaulddin-shammary-dell-andrey-shorov-ericsson
youtube_search_url: https://www.youtube.com/results?search_query=Securing+the+AI%2FML+Lifecycle+With+MLSecOps%3A+Open+Source+Best+Practices+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Securing the AI/ML Lifecycle With MLSecOps: Open Source Best Practices - Bahaulddin Shammary, Dell & Andrey Shorov, Ericsson

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Bahaulddin Shammary, Dell, Andrey Shorov, Ericsson
- Schedule: https://kccnceu2026.sched.com/event/2CW0b/securing-the-aiml-lifecycle-with-mlsecops-open-source-best-practices-bahaulddin-shammary-dell-andrey-shorov-ericsson
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+the+AI%2FML+Lifecycle+With+MLSecOps%3A+Open+Source+Best+Practices+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Securing the AI/ML Lifecycle With MLSecOps: Open Source Best Practices.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW0b/securing-the-aiml-lifecycle-with-mlsecops-open-source-best-practices-bahaulddin-shammary-dell-andrey-shorov-ericsson
- YouTube search: https://www.youtube.com/results?search_query=Securing+the+AI%2FML+Lifecycle+With+MLSecOps%3A+Open+Source+Best+Practices+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=5ZmWuwnv2l4
- YouTube title: Securing the AI/ML Lifecycle With MLSecOps: Open Source Best... Bahaulddin Shammary & Andrey Shorov
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/securing-the-ai-ml-lifecycle-with-mlsecops-open-source-best-practices/5ZmWuwnv2l4.txt
- Transcript chars: 22734
- Keywords: security, process, architecture, machine, learning, secure, specific, reference, important, models, controls, supply, training, stages, ensure, software, personas, pipeline

### Resumo baseado na transcript

I'm a lead AI engineer at Openext and my colleague here >> Andre Shoven, senior security specialist. So together today with Andre, we're uh going to take you through something that matters more each day. Um but what we're going to do then is uh introduce a reference architecture which you can map these stages in the um in the infinity loop. Uh and it can be something like a uh reference architecture or reference uh points um practical ones that you can use. Um and then we're going to layer on the threats uh OASP threats and then we're going to show you some of the security controls you can implement as well as uh some tool suggestions. Um, anyone really who, um, works with machine learning, uh, whether you're cloud professional or, um, a contributor or an engineer, uh, this is for you.

### Excerpt da transcript

Thank you for being here. Um, my name is uh Baja. I'm a lead AI engineer at Openext and my colleague here >> Andre Shoven, senior security specialist. Yeah, I don't want to talk with you about MLOps actually. >> Very nice. I see many people here. So, but how you nervous? >> I I was told there would be less people. So, uh we'll we'll see how this goes. Um, very good. So together today with Andre, we're uh going to take you through something that matters more each day. So and that's um how to actually secure AI and machine learning systems in production. So as organizations rapidly adopt ML, we're seeing a new set of risks emerging and risks that simply don't map to traditional software. Um with traditional software it focuses on um code, you got containers, configurations, but with machine learning the that attack surface um uh explodes. So now you're securing um training data um that can be poisoned. Uh you've got models that can be stolen or tampered with. Um you got pipelines that um retrain continuously which can introduce new risks with every um iteration.

And you've got the inference endpoints which um when exposed um they're exposed to adversarial inputs uh which can be designed to uh you know uh fool your model. So the good news is um we don't have to start from scratch. Um the lessons that we learned from dev sec ops like automation um shared responsibility and security as code um those those principles still apply. So, but what we need to do is extend them and that's what MLSOPS is about. It's dev secops for the machine learning um life cycle. And this talk is based on a white paper uh that myself um and my colleague during our time in Dell and colleagues uh from Ericson um worked on as well as um the a IML open SSF working group. Um so let's get started. Okay. So I'll just quickly walk you through what we are covering today. Uh what we're going to do is um show you one of those infinity loops that you've all seen when it comes to DevOps and MLOps. Um but what we're going to do then is uh introduce a reference architecture which you can map these stages in the um in the infinity loop.

Uh and it can be something like a uh reference architecture or reference uh points um practical ones that you can use. um in your uh work and and then we're going to approach it the same way we did with with the white paper. Um so basically we're going to layer um the personas so the people that are involved at every stage uh you know who's responsible for what. Um
