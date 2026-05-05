---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Application Development"
themes: ["AI ML"]
speakers: ["Kris Coleman", "TestifySec", "Michael Beemer", "Dynatrace"]
sched_url: https://kccncna2025.sched.com/event/27FfH/feature-flag-driven-development-seamlessly-integrate-feature-flags-into-your-sdlc-kris-coleman-testifysec-michael-beemer-dynatrace
youtube_search_url: https://www.youtube.com/results?search_query=Feature+Flag+Driven+Development%3A+Seamlessly+Integrate+Feature+Flags+Into+Your+SDLC+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Feature Flag Driven Development: Seamlessly Integrate Feature Flags Into Your SDLC - Kris Coleman, TestifySec & Michael Beemer, Dynatrace

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Application Development]]
- Temas: [[AI ML]]
- País/cidade: United States / Atlanta
- Speakers: Kris Coleman, TestifySec, Michael Beemer, Dynatrace
- Schedule: https://kccncna2025.sched.com/event/27FfH/feature-flag-driven-development-seamlessly-integrate-feature-flags-into-your-sdlc-kris-coleman-testifysec-michael-beemer-dynatrace
- Busca YouTube: https://www.youtube.com/results?search_query=Feature+Flag+Driven+Development%3A+Seamlessly+Integrate+Feature+Flags+Into+Your+SDLC+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Feature Flag Driven Development: Seamlessly Integrate Feature Flags Into Your SDLC.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FfH/feature-flag-driven-development-seamlessly-integrate-feature-flags-into-your-sdlc-kris-coleman-testifysec-michael-beemer-dynatrace
- YouTube search: https://www.youtube.com/results?search_query=Feature+Flag+Driven+Development%3A+Seamlessly+Integrate+Feature+Flags+Into+Your+SDLC+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=YjAgUlhBV90
- YouTube title: Feature Flag Driven Development: Seamlessly Integrate Feature Flags... Kris Coleman & Michael Beemer
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/feature-flag-driven-development-seamlessly-integrate-feature-flags-int/YjAgUlhBV90.txt
- Transcript chars: 22680
- Keywords: feature, basically, actually, development, management, little, manifest, context, ticket, banner, runtime, application, working, process, around, intent, already, provider

### Resumo baseado na transcript

Um so today we're going to talk about feature flag driven development and how you can seamlessly integrate feature flags into your software delivery life cycle. I've been using feature flags for quite a few years at this point and I serve on the government's committee of open feature. In traditional feature flag systems, you might run into some of these problems. The other problem is we don't know for certain if this flag was a boolean flag. So Coral Health is like the largest healthare system in Michigan and uh my team was tasked with completely redesigning their digital front door app. So the challenge was we needed atomic deploys and we needed safe defaults and we still needed to support the dynamic uh runtime queries.

### Excerpt da transcript

Thank you for joining me today uh for the last session of CubeCon. >> We made it. All right. Yeah, appreciate it. Um so today we're going to talk about feature flag driven development and how you can seamlessly integrate feature flags into your software delivery life cycle. Uh I'm Michael Beamer. I work at Dinatrace as a product manager. I've been using feature flags for quite a few years at this point and I serve on the government's committee of open feature. >> All right. Hellobody. My name is uh >> Yeah, no kidding. How about Oh, is it all right? Hi, I'm Chris Coleman. Uh I'm a director of platform engineering at uh Testify SAC. We're the folks behind uh the Enttools Witness and Archavista, part of the CNCF. Um, and I've been working on continuous delivery and release on demand. I'm a huge champion for future flags. Very passionate about them. [snorts] So, uh, yeah, let's get started. Uh, who here is already using future flags today? Raise your hand. Awesome. That is really exciting. If you haven't already gone and checked out Open Feature, please do.

We're looking for more stars. It's a great great project. Okay. So, if you're using feature flags already, how many of you feel like there is a disconnect between your development flow and your flag ops? Raise your hand. Yeah, it's it's a very very painful part of the adoption process. We're here today to talk about a solution. So, let's talk a little bit about feature flags. Feature flags are powerful. You can do so much with them. Namely, you can separate your deployments from your releases. [snorts] They give you the power of runtime control. You can toggle flags to change the behavior of features and code paths at runtime. They give you the power of progressive rollouts. You can do canary deployments or even uh percentage rollouts. Uh experimentation is super powerful. You can stop making design decisions on your app based on hunches and you can start doing it on real user engagement. Precise targeting. You can change the behavior of features and code paths for precise user segments. But they're not without their challenges.

In traditional feature flag systems, you might run into some of these problems. There's no guarantee that the flag your application code is trying to use actually exists in the upstream provider. Whoops. Uh, runtime errors. You could have typos in your flag name or possibly even a different type of flag. You might expect a boolean, but really the flag is a string or an object or
