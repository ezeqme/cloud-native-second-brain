---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "AI + ML"
themes: ["AI ML", "Kubernetes Core"]
speakers: ["Andrea Giardini", "Crossover Engineering BV"]
sched_url: https://kccnceu2025.sched.com/event/1txAW/kubernetes-and-ai-to-protect-our-forests-a-cloud-native-infrastructure-for-wildfire-prevention-andrea-giardini-crossover-engineering-bv
youtube_search_url: https://www.youtube.com/results?search_query=Kubernetes+and+AI+To+Protect+Our+Forests%3A+A+Cloud+Native+Infrastructure+for+Wildfire+Prevention+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Kubernetes and AI To Protect Our Forests: A Cloud Native Infrastructure for Wildfire Prevention - Andrea Giardini, Crossover Engineering BV

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[AI + ML]]
- Temas: [[AI ML]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Andrea Giardini, Crossover Engineering BV
- Schedule: https://kccnceu2025.sched.com/event/1txAW/kubernetes-and-ai-to-protect-our-forests-a-cloud-native-infrastructure-for-wildfire-prevention-andrea-giardini-crossover-engineering-bv
- Busca YouTube: https://www.youtube.com/results?search_query=Kubernetes+and+AI+To+Protect+Our+Forests%3A+A+Cloud+Native+Infrastructure+for+Wildfire+Prevention+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Kubernetes and AI To Protect Our Forests: A Cloud Native Infrastructure for Wildfire Prevention.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txAW/kubernetes-and-ai-to-protect-our-forests-a-cloud-native-infrastructure-for-wildfire-prevention-andrea-giardini-crossover-engineering-bv
- YouTube search: https://www.youtube.com/results?search_query=Kubernetes+and+AI+To+Protect+Our+Forests%3A+A+Cloud+Native+Infrastructure+for+Wildfire+Prevention+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1rtyQaTfbdM
- YouTube title: Kubernetes and AI To Protect Our Forests: A Cloud Native Infrastructure for Wildf... Andrea Giardini
- Match score: 0.985
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/kubernetes-and-ai-to-protect-our-forests-a-cloud-native-infrastructure/1rtyQaTfbdM.txt
- Transcript chars: 29252
- Keywords: daxter, pipeline, pipelines, wildfire, jupyter, basically, running, feature, started, infrastructure, difficult, platform, couple, always, pretty, resources, notebook, delivery

### Resumo baseado na transcript

We're all tired and everything, but you know, if you're here, you probably want to know something or at least you're curious about how we do wildfire prevention with Kubernetes and AI. And in my free time, I also uh organize community events and yeah, community conferences around Europe. This is extremely time consuming and extremely costly for uh power utility companies. What if instead of instead of going and inspecting those power line visually, what if we do it through satellite images specifically very high resolution satellite imagery and machine learning so that we can get insights from the sky pretty much on how our infrastructure So we have providers that we query and they give us high resolution satellite images. We just used Kubernetes because it was providing us the right balance between flexibility and stability.

### Excerpt da transcript

Good afternoon. Thank you very much for coming to my session today. I know it's one of the last session of CubeCorn. It's Friday. We're all tired and everything, but you know, if you're here, you probably want to know something or at least you're curious about how we do wildfire prevention with Kubernetes and AI. My name is Andre Jardini. I'm a Sens ambassador. I work as an SRE for Overstory. And in my free time, I also uh organize community events and yeah, community conferences around Europe. The title of my talk is Kubernetes and AI to protect our forest, a cloudnative infrastructure for wildfire prevention. Like me, a couple of years ago before I started working for Overtory, I didn't actually know much about wildfires. Wildfires are events that in Europe are a little bit more rare compared to the US just for because of the density, because of the geography of the US territory. But there are events that are extremely destructive for people lives, community, building, businesses and so on. These events are often very sudden.

They happen unpredictably and they bring a lot of destruction to our to our people. Just to give you an idea, just a couple of months ago, I'm sure you're aware, I'm sure you're following the news, a big wildfire spread out in Southern California. This was the second biggest wildfire that happened in California. Over 29 people died, over 200,000 people got evacuated, 18,000 homes destroyed, and over 57,000 acres of land burned down. Just to give you an idea of what 57,000 acres of land means, this is the area that would have burned in London that represents 57,000 acres. And this was not even the largest wildfire that happened in California. The 2018 campfire was uh spread over an area that was almost three times as large, 153,000 acres. Another thing that I didn't know about wildfire is that in California specifically um over 60% of the most destructive wildfires have been caused by defective power lines. I know it sounds curious. I know that we expect you know fire to be you know wildfires to be um caused by you know humans most of the time just you know a cigarette that is not turned down correctly or things like this.

But power lines are actually a big responsible of this kind of wildfire especially in California and wildfire prevention is not an easy task for a multitude of reason. The first one in respect to power lines is that the power infrastructure is very vast. It takes a lot of space. It's very complex. It has a big nu
