---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["Observability"]
speakers: ["Daniel Dyla", "Michael Beemer", "Dynatrace"]
sched_url: https://kccnceu2024.sched.com/event/1YeSC/observable-feature-rollouts-with-opentelemetry-and-openfeature-daniel-dyla-michael-beemer-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Observable+Feature+Rollouts+with+OpenTelemetry+and+OpenFeature+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Observable Feature Rollouts with OpenTelemetry and OpenFeature - Daniel Dyla & Michael Beemer, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[Observability]]
- País/cidade: France / Paris
- Speakers: Daniel Dyla, Michael Beemer, Dynatrace
- Schedule: https://kccnceu2024.sched.com/event/1YeSC/observable-feature-rollouts-with-opentelemetry-and-openfeature-daniel-dyla-michael-beemer-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Observable+Feature+Rollouts+with+OpenTelemetry+and+OpenFeature+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Observable Feature Rollouts with OpenTelemetry and OpenFeature.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeSC/observable-feature-rollouts-with-opentelemetry-and-openfeature-daniel-dyla-michael-beemer-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Observable+Feature+Rollouts+with+OpenTelemetry+and+OpenFeature+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=euYhIn4leW0
- YouTube title: Observable Feature Rollouts with OpenTelemetry and OpenFeature - Daniel Dyla & Michael Beemer
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/observable-feature-rollouts-with-opentelemetry-and-openfeature/euYhIn4leW0.txt
- Transcript chars: 20497
- Keywords: feature, events, database, metrics, little, impact, basically, traces, trace, becomes, actually, analysis, metric, enable, replica, processing, response, looking

### Resumo baseado na transcript

uh I'm Daniel dla um I'm on the open Telemetry governance committee uh I'm also a maintainer of open Telemetry JavaScript I've been working on it for uh a little over four years now uh and I'm a contributor to open feature hi there uh I'm Mike Beamer I'm a product manager at dinet Trace um I'm involved in open source contributions and also a member of the government's committee on open feature and you probably or you may or may not have heard of open fature so I'll really

### Excerpt da transcript

uh I'm Daniel dla um I'm on the open Telemetry governance committee uh I'm also a maintainer of open Telemetry JavaScript I've been working on it for uh a little over four years now uh and I'm a contributor to open feature hi there uh I'm Mike Beamer I'm a product manager at dinet Trace um I'm involved in open source contributions and also a member of the government's committee on open feature and you probably or you may or may not have heard of open fature so I'll really quickly cover what that is um it's it's an open specification for providing vendor agnostic community-driven feature Flags um so it it works with u commercial vendors uh in-house Solutions and maybe something uh you know close Source open source whatever the case may be there's nice Integrations to uh management tools and then if you're not familiar with feature Flags themselves uh I just want to give a really really quick level set here so the main idea is it's a pivot point in your code um it's something that can be updated uh without a a source code change or without a restart to your service themselves so provides a lot of benefits that we'll cover in just a second here so the reasons you may want to use a feature flag is to help coordinate feature releases so you can kind of help decouple uh a binary release from a feature release um it's really common for like trunk based development um you can also reduce the risk of a feature release you can do that in a lot of ways one way is to um control the Imp impact radius it's something we'll show in the demo in a little bit but you could basically enable the feature for a subset of users uh either very specifically or like randomly select a bucket of users to show a feature to and then finally as you kind of get more uh I guess mature in your feature flag usage you may run experiments so you may want to have one two three you know different variations that you'd like to test you'd like to measure that impact and then decide if it's something that you'd like to to keep but with all the benefits of feature Flags it does ruc a few challenges so uh in this uh diagram that we have here we're showing like a really highly distributed like microservice architecture and so we're making lots of calls it's already very complex but if you start adding feature Flags in there you can con you could change like code paths at runtime something that maybe hasn't been tested um you could also have multiple Flags evaluated um on a single request so just it be
