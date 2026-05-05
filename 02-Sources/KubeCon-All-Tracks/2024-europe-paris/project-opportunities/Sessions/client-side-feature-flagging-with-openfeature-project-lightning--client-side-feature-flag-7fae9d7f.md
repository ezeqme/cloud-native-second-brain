---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["Project Opportunities"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQWX/client-side-feature-flagging-with-openfeature-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Client-side+Feature+Flagging+with+OpenFeature+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Client-side Feature Flagging with OpenFeature | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Project Opportunities]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQWX/client-side-feature-flagging-with-openfeature-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Client-side+Feature+Flagging+with+OpenFeature+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Client-side Feature Flagging with OpenFeature | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQWX/client-side-feature-flagging-with-openfeature-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Client-side+Feature+Flagging+with+OpenFeature+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=viBi_X5n8mI
- YouTube title: Client-side Feature Flagging with OpenFeature | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/client-side-feature-flagging-with-openfeature-project-lightning-talk/viBi_X5n8mI.txt
- Transcript chars: 4492
- Keywords: feature, context, flagging, basically, client, vendor, interested, session, allows, change, future, server, everyone, technical, essential, modern, development, control

### Resumo baseado na transcript

all right hi everyone I'm Mike beer I'm a product manager at Dino trace and an open feature maintainer and today I'm excited to tell you about client side feature flagging with open feature let's see hopefully there we go all right so uh sorry about that technical issues all right uh before we dive into the technical details of presentation I just like to do a quick uh level set on what a feature flag is and why we're uh why they're basically essential to Modern soft development practices

### Excerpt da transcript

all right hi everyone I'm Mike beer I'm a product manager at Dino trace and an open feature maintainer and today I'm excited to tell you about client side feature flagging with open feature let's see hopefully there we go all right so uh sorry about that technical issues all right uh before we dive into the technical details of presentation I just like to do a quick uh level set on what a feature flag is and why we're uh why they're basically essential to Modern soft development practices um so a feature flag is a technique that allows you to control a pivot point in your application at runtime uh they do not require the code to be changed or a service to be redeployed or restarted in order for the value to change uh feature Flags allow you to decouple feature releases from deployments and they allow teams to coordinate feature releases on their schedule uh progressively enabling a feature flag allows you to Red reduce risk uh by tightly controlling the impact radius um they also allow you quickly abort uh a failed deployment um by basically instantaneously allowing to revert the change uh teams are also able to experiment using feature Flags by defining the control group and multiple different variations and then testing the impact that the feature has um so really they become very essential to the the whole you know modern software development life cycle uh all right uh then I just really wanted to quickly talk about open Future itself so it's a it's an open uh we're a cncf incubating project um that's created an open specification for vendor agnos vendor agnostic feature flagging um we've created many sdks in popular languages that seamlessly integrate with the commercial Solutions or in-house vendors and then today I'd like to announce that we've uh released a web 1.

SDK this has basically been a long time coming uh we started with uh server side use cases but really we see that you know obviously the web is extremely important to people um and it's been a long time coming to make sure that we can uh support client side and server side feature flagging use cases with a consistent API that's completely vendor agnostic um the web SDK is a foundational SDK that can be used on its own but it also lay the groundwork for framework specific implementations so having a web uh or a vendor neutral web SDK means that everyone can benefit from the SDK regardless of what or where your future flags are managed um and if you're interested definitely take a look at t
