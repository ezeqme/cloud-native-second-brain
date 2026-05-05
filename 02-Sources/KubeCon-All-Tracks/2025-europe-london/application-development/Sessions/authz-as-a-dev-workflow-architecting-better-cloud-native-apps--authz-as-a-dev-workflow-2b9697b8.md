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
themes: ["Application Development"]
speakers: ["Dan \"phrawzty\" Maher", "Cerbos"]
sched_url: https://kccnceu2025.sched.com/event/1tx8s/authz-as-a-dev-workflow-architecting-better-cloud-native-apps-dan-phrawzty-maher-cerbos
youtube_search_url: https://www.youtube.com/results?search_query=Authz+as+a+Dev+Workflow%3A+Architecting+Better+Cloud+Native+Apps+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Authz as a Dev Workflow: Architecting Better Cloud Native Apps - Dan "phrawzty" Maher, Cerbos

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[Application Development]]
- País/cidade: United Kingdom / London
- Speakers: Dan "phrawzty" Maher, Cerbos
- Schedule: https://kccnceu2025.sched.com/event/1tx8s/authz-as-a-dev-workflow-architecting-better-cloud-native-apps-dan-phrawzty-maher-cerbos
- Busca YouTube: https://www.youtube.com/results?search_query=Authz+as+a+Dev+Workflow%3A+Architecting+Better+Cloud+Native+Apps+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Authz as a Dev Workflow: Architecting Better Cloud Native Apps.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx8s/authz-as-a-dev-workflow-architecting-better-cloud-native-apps-dan-phrawzty-maher-cerbos
- YouTube search: https://www.youtube.com/results?search_query=Authz+as+a+Dev+Workflow%3A+Architecting+Better+Cloud+Native+Apps+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=EBbuyn72jtw
- YouTube title: Authz as a Dev Workflow: Architecting Better Cloud Native Apps - Dan "phrawzty" Maher, Cerbos
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/authz-as-a-dev-workflow-architecting-better-cloud-native-apps/EBbuyn72jtw.txt
- Transcript chars: 35115
- Keywords: authorization, security, permissions, actually, checks, permission, business, developer, policy, product, policies, developers, application, access, context, development, important, testing

### Resumo baseado na transcript

Uh, I get to work at Serbos and I get to work at Serbos on open source and before this I worked at lots of neat places like Ubisoft and Mozilla and data dog and I say this only as context to let you understand where I'm coming from for the remainder of this talk. I've gotten to dabble a lot in infrastructure uh and development and also in security. And in this case, transformation made developers more productive whilst simultaneously improving security, improving reliability. Um, well, it hasn't really followed the same evolution path and it's part of the problem is that it's really often deeply coupled with application logic, which I'm going to address in a moment. How developers interact with authorization during development is a big big big element and we can create better security outcomes, better developer experiences and that's what we're going to explore next. We get putting in a security token and that has a big architecture around it, right?

### Excerpt da transcript

Three days. It's long, man. Give yourselves a round of applause. You made it. Heck yeah. All right, I'm going to start the timer. I said I'd forget it and I didn't. Nice. Hi everybody. My name is Dan. I work at a company called Serbos. This is CubeCon in London in 2025. That is my title slide. Thanks for joining me today. Uh, I get to work at Serbos and I get to work at Serbos on open source and before this I worked at lots of neat places like Ubisoft and Mozilla and data dog and I say this only as context to let you understand where I'm coming from for the remainder of this talk. I've gotten to dabble a lot in infrastructure uh and development and also in security. And a thing that I've learned uh along this path, I've learned a lot of things, but one of those things is that authorization, different from authentication, thank you very much, isn't just a security problem, although it's often relegated to that. It's actually a developer experience problem as well. And that's really what I want to talk about today.

Um let's start with what I call, and I'm not the only one who calls it this is the authorization paradox. Okay, every single request in every single application, especially in today's modern whisbang cloudnative environment, right, needs to answer the question at every single encounter, is this user allowed to do this thing under what conditions, right? It's unavoidable. It's important for security, but authorization is actually treated as an afterthought uh in our architectures and our workflows, especially as developers, especially even as infrastructure people. And we've actually seen this pattern before. Uh I'm a man of a certain age and I remember when deploying was just a collection of bash scripts or like setting and grepping and stuff like this, right? Um you probably remember when observability meant grepping through log files as opposed to like a single pain. You got your graphana and your data dog and stuff right now. Uh our industry basically recognized these pain points and was like we don't want to feel this pain anymore.

What can we do? But authorization hasn't gone through this elegant developer transformation yet, right? It remains stuck in this sort of a weird strange place. It's something that every developer has to implement, but few have good tools or or patterns really for building it, right? So it creates friction rather than flow. And when something creates friction, we find ways around it and sometimes not very good ways
