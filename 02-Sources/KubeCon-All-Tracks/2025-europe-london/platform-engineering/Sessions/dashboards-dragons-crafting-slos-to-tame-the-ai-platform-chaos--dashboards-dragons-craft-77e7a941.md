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
themes: ["AI ML", "Observability", "Platform Engineering"]
speakers: ["Alexa Griffith", "Ankita Chaudhari", "Bloomberg"]
sched_url: https://kccnceu2025.sched.com/event/1tx75/dashboards-dragons-crafting-slos-to-tame-the-ai-platform-chaos-alexa-griffith-ankita-chaudhari-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Dashboards+%26+Dragons%3A+Crafting+SLOs+To+Tame+the+AI+Platform+Chaos+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Dashboards & Dragons: Crafting SLOs To Tame the AI Platform Chaos - Alexa Griffith & Ankita Chaudhari, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Observability]], [[Platform Engineering]]
- País/cidade: United Kingdom / London
- Speakers: Alexa Griffith, Ankita Chaudhari, Bloomberg
- Schedule: https://kccnceu2025.sched.com/event/1tx75/dashboards-dragons-crafting-slos-to-tame-the-ai-platform-chaos-alexa-griffith-ankita-chaudhari-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Dashboards+%26+Dragons%3A+Crafting+SLOs+To+Tame+the+AI+Platform+Chaos+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Dashboards & Dragons: Crafting SLOs To Tame the AI Platform Chaos.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx75/dashboards-dragons-crafting-slos-to-tame-the-ai-platform-chaos-alexa-griffith-ankita-chaudhari-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Dashboards+%26+Dragons%3A+Crafting+SLOs+To+Tame+the+AI+Platform+Chaos+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=KyoxaAtHi-c
- YouTube title: Dashboards & Dragons: Crafting SLOs To Tame the AI Platform Cha... Alexa Griffith & Ankita Chaudhari
- Match score: 0.859
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dashboards-dragons-crafting-slos-to-tame-the-ai-platform-chaos/KyoxaAtHi-c.txt
- Transcript chars: 27223
- Keywords: platform, latency, inference, metrics, dashboards, observability, performance, actually, across, dashboard, infrastructure, request, slo, throughput, success, within, window, reliability

### Resumo baseado na transcript

Welcome and we're very happy and excited to be here today and to present to you our talk dashboards and dragons crafting SLOs's to tame the AI platform chaos at scale. So welcome brave adventures to our quest where we'll craft the SLOs's to vanquish the chaos haunting our AI realms. So this helps us to clearly navigate trade-offs uh and reliability, innovation and velocity. You know you chop off one head like inconsistent deployments and two more heads pop up like security or observability issues. We use the envoy gateway and we use that to be able to serve you know onrem a manage manage inference uh kubernetes cluster and we use kserve with that but also we use it to easily be able to hit any other lm provider that you need. So these metrics define user experience and ensure that our platform delivers on uh promised reliability, latency and performance.

### Excerpt da transcript

Welcome and we're very happy and excited to be here today and to present to you our talk dashboards and dragons crafting SLOs's to tame the AI platform chaos at scale. So welcome brave adventures to our quest where we'll craft the SLOs's to vanquish the chaos haunting our AI realms. My name is Alexa Griffith and I am a senior software engineer at Bloomberg. I work on uh building our AI inference platform. My name is Ankita and I'm a senior product manager at Bloomberg. Um, I focus mostly on our computer infrastructure. Nice. So, our quest begins. Um, as you can tell, I had a little bit of fun making these doodles for this presentation. So, let's check out our treasure map for today's journey. We're going to tackle the Genai Hydra, peer into the crystal ball of observability, and then venture deep into the dashboard uh dungeon and defend against the fortress of platform challenges. First, a little bit about AI platforms at Bloomberg. We service the whole model development life cycle. So from exploration with the data to building your model and experimentation to deployment serving and then um model maintenance and production for monitoring updating.

So what this looks like is various platform teams and services um within our AI within AI platforms. So we offer services like Jupyter notebooks um different ways to train and use HPC manage serving managed inference and different AI pipelines and tools to our users. So let's get into SLOs's. Think of SLOs's as ancient runes, each holding the magic to illuminate the health of your platform. So decoding these runes can give us clarity in uncertain times. So what makes up an SLO? First, a service level indicator SLI. This is a metric generated by query. So an example is latency, throughput or error rates, what you want to measure. Then you have an objective. So that's the desired performance for that SLI. So if it's latency, we want our latency to be under 50 milliseconds, for example. Next, we'll have a target value. So how often must this objective be met? So 99.99 999% of the time, for example. Next, how do we measure it? With a time window. That's so that's the duration over which the target value is measured.

For example, over a two-hour window, over the last 24 hours. So just like any magic potion um SLOs's combine carefully chosen ingredients. So what we need is a common language between our engineers uh operations and stakeholders. We want it to be user focused. So we want to highlight real impact and al
