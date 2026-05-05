---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Cloud Native Novice"
themes: ["Security", "SRE Reliability"]
speakers: ["Jakub Krzywda", "Elastisys"]
sched_url: https://kccnceu2026.sched.com/event/2CVzd/cloud-native-non-functional-requirements-building-scalable-resilient-and-secure-applications-jakub-krzywda-elastisys
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Non-Functional+Requirements%3A+Building+Scalable%2C+Resilient+and+Secure+Applications+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Non-Functional Requirements: Building Scalable, Resilient and Secure Applications - Jakub Krzywda, Elastisys

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Security]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jakub Krzywda, Elastisys
- Schedule: https://kccnceu2026.sched.com/event/2CVzd/cloud-native-non-functional-requirements-building-scalable-resilient-and-secure-applications-jakub-krzywda-elastisys
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Non-Functional+Requirements%3A+Building+Scalable%2C+Resilient+and+Secure+Applications+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Non-Functional Requirements: Building Scalable, Resilient and Secure Applications.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CVzd/cloud-native-non-functional-requirements-building-scalable-resilient-and-secure-applications-jakub-krzywda-elastisys
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Non-Functional+Requirements%3A+Building+Scalable%2C+Resilient+and+Secure+Applications+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=GXa_jTamRo0
- YouTube title: Cloud Native Non-Functional Requirements: Building Scalable, Resilient and Secure... Jakub Krzywda
- Match score: 0.966
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-non-functional-requirements-building-scalable-resilient-a/GXa_jTamRo0.txt
- Transcript chars: 19086
- Keywords: application, security, platform, applications, requirements, cloudnative, developers, database, platforms, ensure, non-functional, changes, components, implement, provide, continuous, deployment, principle

### Resumo baseado na transcript

I would like um all of you to imagine uh that you have recently been asked to design an architecture of an application. Uh you pull out the marker and you know that little moment the cap comes off and there is a click. uh we are leaving the comforting boxes behind and focus on making sure that we design the guarantees uh what the platform can give you and what the application still has to earn. I'm Yakub Shiva uh cloudnative architect at Elasticis and I will share with you today lessons learned over many years of fulfilling non-functional requirements while building scalable, resilient and secure systems on top of application platforms. The goals of this talk are to explore the relationship among uh guiding principles, architecture approaches, requirements and implementation details within the realm of cloudnative technologies and to provide you uh application developers with practical insights on how to build applications which are not only Second, uh scaled agile defines non-functional requirements as system qualities that guide the design of the solution and often serve as constraints.

### Excerpt da transcript

I would like um all of you to imagine uh that you have recently been asked to design an architecture of an application. You are now standing in a meeting room in front of a clean whiteboard. Uh you pull out the marker and you know that little moment the cap comes off and there is a click. Then uh you start when everyone starts. You draw boxes. User uh interacts with the front end box that talks to the API box that writes to the database. Another box. This is the comforting path, the functional story. Uh what the application does, how data moves, the happy path. But then you hesitate for a brief moment. If you keep uh going like this uh you will build uh something that work works beautifully the first time uh with 10 users on your laptop. So you switch uh the marker color uh because that's the sign that we are about to switch uh the perspective. and you write three words uh on top of the board. Scale, resilience, security. Uh you ask yourself what happens uh when marketing campaign is successful and application traffic increases 20 times on day one.

Uh what if one failed component takes the whole system down? Are we at risk of leaking uh user data due to vulnerabilities in our software stack? Now the boxes on the board don't change much but uh the design changes completely because functional requirements tell you what the system should do and non-functional requirements decide where whether you can keep going under load under failure and under attack. That's uh what this uh talk is about. uh we are leaving the comforting boxes behind and focus on making sure that we design the guarantees uh what the platform can give you and what the application still has to earn. I'm Yakub Shiva uh cloudnative architect at Elasticis and I will share with you today lessons learned over many years of fulfilling non-functional requirements while building scalable, resilient and secure systems on top of application platforms. The goals of this talk are to explore the relationship among uh guiding principles, architecture approaches, requirements and implementation details within the realm of cloudnative technologies and to provide you uh application developers with practical insights on how to build applications which are not only functional but built to past.

This talk consists of three parts. First, I will uh provide a context defining cloud native non-functional requirements and application platforms. Second, I will discuss various approaches and principles that help us t
