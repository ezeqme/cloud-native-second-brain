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
themes: ["AI ML", "Observability", "Community Governance"]
speakers: ["Dotan Horovits", "OpenObservability Talks", "Adriel Perkins", "Liatrio"]
sched_url: https://kccnceu2025.sched.com/event/1tcxP/standardizing-cicd-observability-with-opentelemetry-insights-from-the-cicd-observability-sig-dotan-horovits-openobservability-talks-adriel-perkins-liatrio
youtube_search_url: https://www.youtube.com/results?search_query=Standardizing+CI%2FCD+Observability+With+OpenTelemetry%3A+Insights+From+the+CI%2FCD+Observability+SIG+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Standardizing CI/CD Observability With OpenTelemetry: Insights From the CI/CD Observability SIG - Dotan Horovits, OpenObservability Talks & Adriel Perkins, Liatrio

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Dotan Horovits, OpenObservability Talks, Adriel Perkins, Liatrio
- Schedule: https://kccnceu2025.sched.com/event/1tcxP/standardizing-cicd-observability-with-opentelemetry-insights-from-the-cicd-observability-sig-dotan-horovits-openobservability-talks-adriel-perkins-liatrio
- Busca YouTube: https://www.youtube.com/results?search_query=Standardizing+CI%2FCD+Observability+With+OpenTelemetry%3A+Insights+From+the+CI%2FCD+Observability+SIG+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Standardizing CI/CD Observability With OpenTelemetry: Insights From the CI/CD Observability SIG.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcxP/standardizing-cicd-observability-with-opentelemetry-insights-from-the-cicd-observability-sig-dotan-horovits-openobservability-talks-adriel-perkins-liatrio
- YouTube search: https://www.youtube.com/results?search_query=Standardizing+CI%2FCD+Observability+With+OpenTelemetry%3A+Insights+From+the+CI%2FCD+Observability+SIG+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=IvIgsHS5MDk
- YouTube title: Standardizing CI/CD Observability With OpenTelemetry: Insights Fr... Dotan Horovits & Adriel Perkins
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/standardizing-ci-cd-observability-with-opentelemetry-insights-from-the/IvIgsHS5MDk.txt
- Transcript chars: 22556
- Keywords: actually, semantic, pipelines, observability, attributes, traces, repository, metrics, github, exactly, period, another, maintainers, gitlab, adriel, running, looking, screenshot

### Resumo baseado na transcript

Uh I just wish there was a really a better way to figure this stuff out. if it's any encouragement you know uh I've been suffering for that from years you know CI/CD observability uh actually curious who here has suffered from uh lack of observability and CI/CD pipelines okay so as you can see you're not the only one we're how your telemetry is represented in the different signals logs metrics traces span data uh and what's the relationship also between the signals right yeah exactly so you think about like a common microser architecture probably communicating over the network semantic conventions is going to define some of the fields that you may attach to those communication so you can observe them in a consistent way across the board another example might be tracing within GitHub or git lab pipelines where you could analyze them based off of a set So, this is a set of metrics called the VCS, which stands for version control system metrics. But these would be the repository metrics uh for the semantic inventions and they have quite a few open changes but they're doing as they're going as fast as they can and uh it's it's nice to be able to have these things because once we can visualize them we can try to improve them if if the need fits.

### Excerpt da transcript

Yo, Adriel, what's up, man? Why do you look so depressed? Well, I got another uh Slack message. Apparently, there are some things going on with our pipelines. And then someone asked me to figure out what's going on. Uh I just wish there was a really a better way to figure this stuff out. You know, like apply basic SR fundamentals, but to our pipelines. Don't worry about that. It's It's not just you. if it's any encouragement you know uh I've been suffering for that from years you know CI/CD observability uh actually curious who here has suffered from uh lack of observability and CI/CD pipelines okay so as you can see you're not the only one we're in the same boat together and and actually not just in the workplace you know even us as maintainers suffer that day in and day out and uh this is actually an example from just over a week ago we were uh at the hotel maintainers Slack channel and you know uh complaining about uh what goes on here. The the CI on this PR is taking way too long to find the runners for the running the tests.

Sounds familiar. Sounds familiar. So that's also in open source suffering the same thing. And I've been complaining about that for years. Uh which drove me about a couple of years ago to raise the pain of um know not just importance of CI/CD observability but also to standardize on this and uh to be honest no better place than open telemetry. Open telemetry that's that observability framework thing right? Yeah, exactly. That's that's today the uh essentially the de facto standard for uh for instrumenting for emitting for collecting telemetry data from your applications. Everyone uses that today in produ monitoring production environments. So why not do exactly that also for CCD pipelines. So that led to this uh uh OTP open telemetry enhancement proposal that uh came up about two years ago to do exactly that. Well, I'm looking at this quite handy screenshot you have here, but I'm seeing uh that it was closed, not merged. So, what happened to that? Okay, you got me there. But uh good end to the story. this uh OTP, this open telemetry enhancement proposal ended up with the another proposal to form a special interest group, a SIG dedicated to exactly that to standardizing on CI/CD observability that actually you and I started together.

So, so that happened about uh over a year ago now. Very cool. And recently uh we actually wrote a blog post on the CNCF foundation. You can check it out there through the QR code. Um but it's centered
