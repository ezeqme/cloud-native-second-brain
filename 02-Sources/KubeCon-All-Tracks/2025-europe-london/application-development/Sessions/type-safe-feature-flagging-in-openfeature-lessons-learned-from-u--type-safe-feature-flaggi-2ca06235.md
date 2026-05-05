---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["AI ML"]
speakers: ["Michael Beemer", "Dynatrace", "Florin-Mihai Anghel", "Google"]
sched_url: https://kccnceu2025.sched.com/event/1txHF/type-safe-feature-flagging-in-openfeature-lessons-learned-from-using-feature-flags-at-google-michael-beemer-dynatrace-florin-mihai-anghel-google
youtube_search_url: https://www.youtube.com/results?search_query=Type-safe+Feature+Flagging+in+OpenFeature%3A+Lessons+Learned+From+Using+Feature+Flags+at+Google+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Type-safe Feature Flagging in OpenFeature: Lessons Learned From Using Feature Flags at Google - Michael Beemer, Dynatrace & Florin-Mihai Anghel, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]]
- País/cidade: United Kingdom / London
- Speakers: Michael Beemer, Dynatrace, Florin-Mihai Anghel, Google
- Schedule: https://kccnceu2025.sched.com/event/1txHF/type-safe-feature-flagging-in-openfeature-lessons-learned-from-using-feature-flags-at-google-michael-beemer-dynatrace-florin-mihai-anghel-google
- Busca YouTube: https://www.youtube.com/results?search_query=Type-safe+Feature+Flagging+in+OpenFeature%3A+Lessons+Learned+From+Using+Feature+Flags+at+Google+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Type-safe Feature Flagging in OpenFeature: Lessons Learned From Using Feature Flags at Google.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txHF/type-safe-feature-flagging-in-openfeature-lessons-learned-from-using-feature-flags-at-google-michael-beemer-dynatrace-florin-mihai-anghel-google
- YouTube search: https://www.youtube.com/results?search_query=Type-safe+Feature+Flagging+in+OpenFeature%3A+Lessons+Learned+From+Using+Feature+Flags+at+Google+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=mewXGSwDCE4
- YouTube title: Type-safe Feature Flagging in OpenFeature: Lessons Learned F... Michael Beemer & Florin-Mihai Anghel
- Match score: 0.811
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/type-safe-feature-flagging-in-openfeature-lessons-learned-from-using-f/mewXGSwDCE4.txt
- Transcript chars: 27843
- Keywords: feature, basically, google, pretty, hopefully, management, application, source, usually, introduce, default, binary, developer, present, little, release, particular, trying

### Resumo baseado na transcript

Uh today we are going to talk about type safe feature flagging in open feature and kind of the lessons that we were learning across at Google. Uh my name is Floren and I've been a software engineer at Google for three years and my work was kind of revolving around feature flags and making rollouts across Google Cloud Platform safer. If you figure out something goes wrong into production, just, you know, quickly disable the feature, ramp it down, and the problem is is is mitigated. different name and you know when trying to query the value for this flag we cannot find it in our flag management system then what well in that case u you know you would default to the code default value which is true. So your app is querying the flag service and trying to figure out like what is the value for your feature flag. Um and we in with those problems also came like with all those challenges not just something like you know what if the you know these are things which we actually came across.

### Excerpt da transcript

Hello everybody. Uh welcome to our talk. Uh today we are going to talk about type safe feature flagging in open feature and kind of the lessons that we were learning across at Google. Uh my name is Floren and I've been a software engineer at Google for three years and my work was kind of revolving around feature flags and making rollouts across Google Cloud Platform safer. And for a while now I've been an active open source contributor in this project that we're going to talk about today. Hi there. Uh I'm Mike Beamer. I'm a product manager at Dinatrace. I've been you know in software for quite a while now with a number of different roles. I'm a active open source contributor. I'm also a co-founder of open feature and on the governance committee. That's very cool. So I'm going to start off with one question towards all of you. Uh I'm wondering who here is using feature flags in their code uh and who's here has used a feature flag in their code. Why? No, I'm kidding. Feature flags are really really cool and hopefully if you're using them you get to keep using them and uh yeah so you know just to walk you a little bit through the agenda I'm going to talk about for those of you who don't know what feature flags are I'm going to talk a little bit about them I'm going to talk about how we are using feature flags at Google uh our approach and a few lessons that we've learned across the way and some findings that you know we thought would be useful to share with everybody uh and then Mike is going to walk you through the code generation open feature CLI the thing we're here to show you today and you know stay tuned until to the very end to find out how you can use it and more even importantly how you can also contribute to it if you like what you see here.

Um cool. So what is a feature flag? Um feature flags kind of represent this uh very very cool way to uh you know kind of dynamically change the behavior of your binary without creating a new binary release every time. Right? We are allowed to dynamically enable or disable a particular a particular uh a particular feature and you don't have to modify the the source code. Um so what is the advantage of something like this? Uh I think the biggest advantage that there is is to allow for progre more progressive rollouts of feature flags. So it allows more granularity that you you couldn't do with a binary release. You know you could slowly slowly slowly gradually enable a new feature feature or functionality of your
