---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Scott Nichols", "Chainguard"]
sched_url: https://kccnceu2022.sched.com/event/ytqa/thinking-cloud-native-cloudevents-future-scott-nichols-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Thinking+Cloud+Native%2C+CloudEvents+Future+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Thinking Cloud Native, CloudEvents Future - Scott Nichols, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Scott Nichols, Chainguard
- Schedule: https://kccnceu2022.sched.com/event/ytqa/thinking-cloud-native-cloudevents-future-scott-nichols-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Thinking+Cloud+Native%2C+CloudEvents+Future+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Thinking Cloud Native, CloudEvents Future.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqa/thinking-cloud-native-cloudevents-future-scott-nichols-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Thinking+Cloud+Native%2C+CloudEvents+Future+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Y6D0AY5aK-4
- YouTube title: Thinking Cloud Native, CloudEvents Future - Scott Nichols, Chainguard
- Match score: 0.842
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/thinking-cloud-native-cloudevents-future/Y6D0AY5aK-4.txt
- Transcript chars: 31725
- Keywords: events, protocol, produce, custom, object, working, trying, little, schema, routing, projects, version, serverless, integrations, another, language, define, payload

### Resumo baseado na transcript

okay uh this is thinking cloud native cloud events future it's the serverless uh or the cncf serverless working group update um mostly focused around cloud events so if you're in the wrong spot it's a long walk uh i thought i'd give a quick tldr of how we got here and then i'll move on to something completely different than we've done in other working group updates uh it's super quick you know we we as a group the community wrote a white paper in 2018 started in 2017

### Excerpt da transcript

okay uh this is thinking cloud native cloud events future it's the serverless uh or the cncf serverless working group update um mostly focused around cloud events so if you're in the wrong spot it's a long walk uh i thought i'd give a quick tldr of how we got here and then i'll move on to something completely different than we've done in other working group updates uh it's super quick you know we we as a group the community wrote a white paper in 2018 started in 2017 and the result of that was things like this cncf serverless landscape box that has been updated and in 2019 one of the results of that paper was it's really difficult to use serverless because there's no standard definition of how events get to functions so to try to address that the cloud event spec was created and we'll go back into more detail right now so this is the serverless landscape that was originally created there's a bunch of research through uh a lot of people in the cncf community and uh red point and of course it's evolved a lot since uh four or five years from then in fact there's not a lot of similar pictures on this fiction it's it's it's it's crazy um and really great and you know now we have cloud events here and that's what we're here to talk about but of course we are trying to do all of this cloud native compute technology because we want to be able to take these projects and assemble them into some very complex system and one of the one of the things that the cncf is trying to promise is that these things come off the shelf they wire together and you can get up and going with very very little friction and so we started looking around and i'm going to show you a couple examples of excellent projects and i just noticed a little something that was recurring and that's that they almost every project has either the ability to consume an event or or the ability to produce an event so prometheus has this alert manager and i'm not totally sure what's in that box but you know if we zoom in presumably it's pushing events to some sort of persistent layer and then there's a bunch of custom code that sends to pagerduty and email and probably slack and all these other tight integrations that prometheus is now has to manage we can move on to kubej and in fact they have another eventing bus system here and it could be that mqtt is the absolute correct solution for them but you know it brings questions like do they have to manage that can i bring my own could i bring a different version
