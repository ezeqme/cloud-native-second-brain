---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Application Development"
themes: ["Kubernetes Core"]
speakers: ["Harshvardhan Parmar", "YosemiteCrew", "Anushka Saxena", "Google"]
sched_url: https://kccnceu2026.sched.com/event/2CW31/dynamic-mocking-for-event-driven-apis-a-cloud-native-approach-with-kubernetes-harshvardhan-parmar-yosemitecrew-anushka-saxena-google
youtube_search_url: https://www.youtube.com/results?search_query=Dynamic+Mocking+for+Event-Driven+APIs%3A+A+Cloud+Native+Approach+With+Kubernetes+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Dynamic Mocking for Event-Driven APIs: A Cloud Native Approach With Kubernetes - Harshvardhan Parmar, YosemiteCrew & Anushka Saxena, Google

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Application Development]]
- Temas: [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Harshvardhan Parmar, YosemiteCrew, Anushka Saxena, Google
- Schedule: https://kccnceu2026.sched.com/event/2CW31/dynamic-mocking-for-event-driven-apis-a-cloud-native-approach-with-kubernetes-harshvardhan-parmar-yosemitecrew-anushka-saxena-google
- Busca YouTube: https://www.youtube.com/results?search_query=Dynamic+Mocking+for+Event-Driven+APIs%3A+A+Cloud+Native+Approach+With+Kubernetes+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Dynamic Mocking for Event-Driven APIs: A Cloud Native Approach With Kubernetes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW31/dynamic-mocking-for-event-driven-apis-a-cloud-native-approach-with-kubernetes-harshvardhan-parmar-yosemitecrew-anushka-saxena-google
- YouTube search: https://www.youtube.com/results?search_query=Dynamic+Mocking+for+Event-Driven+APIs%3A+A+Cloud+Native+Approach+With+Kubernetes+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=vS0AY3FJfcg
- YouTube title: Dynamic Mocking for Event-Driven APIs: A Cloud Native Approa... Harshvardhan Parmar & Anushka Saxena
- Match score: 0.84
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/dynamic-mocking-for-event-driven-apis-a-cloud-native-approach-with-kub/vS0AY3FJfcg.txt
- Transcript chars: 16470
- Keywords: basically, created, dynamic, event-driven, native, micros, driven, systems, examples, consume, dynamically, please, values, microsoft, discussed, random, events, mocking

### Resumo baseado na transcript

I hope you all had a good lunch and um, I suppose no one's going to sleep midway. Um, so today I'm here to talk about how you can do dynamic mocking for event-driven APIs using our own very cloudnative um tool called micros micro and um so this talk was supposed to be with my co-speaker Harshwadin but unfortunately he couldn't um How many of you use uh event-driven architecture with your um uh production systems? And uh if you have a solution to this problem, uh I'd love to discuss more about it later on. So um since all of these um messaging stuff is uh is the new backbone of our microservices uh and our ribbon driven architectures we have to have something to test it right because I mean we can always test on the broad uh but Yeah, I uh so yeah um I I I saw uh no raise of hand when I said is it easy to test your um your event driven architectures in uh before you you roll them to the prod.

### Excerpt da transcript

Hello everyone. Um, a very good afternoon to all of you. I hope you all had a good lunch and um, I suppose no one's going to sleep midway. Even if you do, that's fine. I'm not going to tell anyone. Um, so today I'm here to talk about how you can do dynamic mocking for event-driven APIs using our own very cloudnative um tool called micros micro and um so this talk was supposed to be with my co-speaker Harshwadin but unfortunately he couldn't um be here in person due to some visa issues and stuff um but so it's just me today but Let's get going. Uh, I actually have something from Harshwaden. Hey everyone, Hashwad on this side. I hope you guys are enjoying CubeCon and I'm already missing it too much. So that's why I'm wearing my last CubeCon t-shirt. Uh thank you so much for coming out to listen our talk and hopefully you guys will like it and please feel free to share your thoughts uh with me with Anushka and with the Microsoft community. I hope we'll see you soon again. >> All right. So um we definitely missing him but the show must go on.

So um Harward is a um am I audible with this? Okay. So um Harshwaran is a maintainer at the micro um project and um he uh he was about to give a demo um about a few things that we'll be discussing um in a few minutes um and a little bit about me. I am Anushka Sakina. I am a software application developer uh developer apprentice at Google. And uh just to let you know that uh this is nothing related to what I do at my job or um um my employer has to do nothing with this. So um just a disclaimer that we have to give all the time and I have been um a mentee at the async API project um which uh which helps us to to provide the API spec for event-driven APIs and I have been a contributor to micro as well and uh I've done latest um my LFX mentorship with the cloud native PG projects. So let's get going. All right. Um, so we see messages everywhere. How many of you use uh event-driven architecture with your um uh production systems? Can I just have a raise? My god, that's a lot. Okay, so that that pretty much explains why we are here.

So um how how often do you think that um um it's uh how easy it is for you? Um okay, uh let me put it in a different way. Do you think it's very easy for you to to mock your uh um event-driven APIs um and like just just test them? Is it that quick and easy? Do you think anyone? And uh if you have a solution to this problem, uh I'd love to discuss more about it later on. But yeah, so um we see wher
