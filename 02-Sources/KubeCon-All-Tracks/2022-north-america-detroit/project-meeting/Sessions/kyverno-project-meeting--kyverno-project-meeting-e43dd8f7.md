---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Project Meeting"
themes: ["Project Meeting"]
speakers: []
sched_url: https://kccncna2022.sched.com/event/1BaTH/kyverno-project-meeting
youtube_search_url: https://www.youtube.com/results?search_query=Kyverno+Project+Meeting+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Kyverno Project Meeting

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Project Meeting]]
- Temas: [[Project Meeting]]
- País/cidade: United States / Detroit
- Speakers: N/A
- Schedule: https://kccncna2022.sched.com/event/1BaTH/kyverno-project-meeting
- Busca YouTube: https://www.youtube.com/results?search_query=Kyverno+Project+Meeting+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Kyverno Project Meeting.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/1BaTH/kyverno-project-meeting
- YouTube search: https://www.youtube.com/results?search_query=Kyverno+Project+Meeting+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=UV7HN6WRcMs
- YouTube title: Kyverno Contributor Meeting
- Match score: 0.72
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/kyverno-project-meeting/UV7HN6WRcMs.txt
- Transcript chars: 16590
- Keywords: policy, running, update, controller, leader, report, issues, kirino, generate, anything, questions, meeting, contributors, resources, instance, already, working, release

### Resumo baseado na transcript

okay we're on youtube right now um hello everyone welcome to the kirono contributors meeting today is may 27th um so i'm shootings out by the way i'm the maintainer of the kirino project today um i'll be giving an ajay update uh of the implementation and then if you have any topic one to discuss in this meeting please feel free to add to the agenda and uh before we started please add yourself to the attendees okay um so like as we discussed in the previous contributors meeting

### Excerpt da transcript

okay we're on youtube right now um hello everyone welcome to the kirono contributors meeting today is may 27th um so i'm shootings out by the way i'm the maintainer of the kirino project today um i'll be giving an ajay update uh of the implementation and then if you have any topic one to discuss in this meeting please feel free to add to the agenda and uh before we started please add yourself to the attendees okay um so like as we discussed in the previous contributors meeting we started aha implementation uh for the high availability support um the logic we proposed before is was that um we want to enable the leader election in each individual controller of kubernetes so while we implement that approach we found one issue with that is since we use the informers in most of the kibo controllers to add the event handler as well as to load the cash for the target resources it is not guaranteed that when the leader the cash when the leader is lag is elected the cache is like loaded loaded the the objects are loaded in the cache so that brings us a problem during the first reconciliation of each controller the leader could look lose that events that resource events so take the policy controller as an example to know we during the kivernal start we will load all the existing resources as well as the policies and then apply those policies to the resource but with the approach we we came up with before the problem is that the leader could lose the events for the for those policies that are added to the cash so the policy report will be only be recovered after like the next in the next reconciliation of the of the office controller so that is roughly one hour later this is apparently not the expected behavior so we kind of changed we also looked at other projects out there using the leader election as well as the how kubernetes principle plan implements this leader election we found that the best approach is to just enable the leader election per instance or to say per pot so that at a time you will be guaranteed there is only one leader running running all the time and all the controllers in this instance will do its job so that's kind of the approach right now we are implementing and uh there is a pr already created it's work in progress but um we've d we've done the basic text for that for the web hook uh components as well as the policy controller we found it's it's pretty reliable on that so um we're still working on the change of the generate controller but w
