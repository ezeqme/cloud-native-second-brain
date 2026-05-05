---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Operations + Performance"
themes: ["SRE Reliability"]
speakers: ["Muvaffak Onuş", "QA Wolf"]
sched_url: https://kccnceu2024.sched.com/event/1YeP3/the-party-must-go-on-resume-pods-after-spot-instance-shut-down-muvaffak-onus-qa-wolf
youtube_search_url: https://www.youtube.com/results?search_query=The+Party+Must+Go+on+-+Resume+Pods+After+Spot+Instance+Shut+Down+CNCF+KubeCon+2024
slides: []
status: parsed
---

# The Party Must Go on - Resume Pods After Spot Instance Shut Down - Muvaffak Onuş, QA Wolf

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Operations + Performance]]
- Temas: [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: Muvaffak Onuş, QA Wolf
- Schedule: https://kccnceu2024.sched.com/event/1YeP3/the-party-must-go-on-resume-pods-after-spot-instance-shut-down-muvaffak-onus-qa-wolf
- Busca YouTube: https://www.youtube.com/results?search_query=The+Party+Must+Go+on+-+Resume+Pods+After+Spot+Instance+Shut+Down+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre The Party Must Go on - Resume Pods After Spot Instance Shut Down.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeP3/the-party-must-go-on-resume-pods-after-spot-instance-shut-down-muvaffak-onus-qa-wolf
- YouTube search: https://www.youtube.com/results?search_query=The+Party+Must+Go+on+-+Resume+Pods+After+Spot+Instance+Shut+Down+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=c2MbSM9-7Xs
- YouTube title: The Party Must Go on - Resume Pods After Spot Instance Shut Down - Muvaffak Onuş, QA Wolf
- Match score: 0.935
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/the-party-must-go-on-resume-pods-after-spot-instance-shut-down/c2MbSM9-7Xs.txt
- Transcript chars: 26132
- Keywords: checkpoint, process, container, restore, processes, running, effectively, support, second, option, another, actually, browser, taking, available, directory, upstream, volume

### Resumo baseado na transcript

so uh the talk is about resuming pots after sport instance shutdown down the with the cheeky title of the party must go on um so who am I I'm muaf I'm an engineer at QA wolf and a Meritus maintainer at crossplane which is a cncf project and I've been involved in cncf commit since about like 2019 um so I work at quolf what what is quolf quolf has a platform that runs all these QA tests browser tests and a group of Engineers in-house QA Engineers that so our first goal is going to be running creu in container and we're just going to go over like you know the problems that we faced when we tried to do that so the first problem is the PID collusion problem when you start

### Excerpt da transcript

so uh the talk is about resuming pots after sport instance shutdown down the with the cheeky title of the party must go on um so who am I I'm muaf I'm an engineer at QA wolf and a Meritus maintainer at crossplane which is a cncf project and I've been involved in cncf commit since about like 2019 um so I work at quolf what what is quolf quolf has a platform that runs all these QA tests browser tests and a group of Engineers in-house QA Engineers that writes and maintains those tests together we make up the qaol team where we can provide you High coverage with zero effort effectively company comes to qu evolve hey we want our web apps to be tested and we write the test we maintain them we schedule them uh we just tell you about the bugs um and it's the high velocity and that gives you like you know confidence to to ship much more frequently so this is an example um playground uh on the left you see that we use like playright test usual browser test code and on the right you're you're seeing the logs and the the browser page um so in order to do that at our scale we are running over 2 million test every month uh that means hundreds of nodes um so in order to in order for this to be affordable we're using spot instances in Google Cloud which gives you like you know about 40 to 60% cost reduction um but the main thing with spot instances is that they fail randomly they just restart and like you know Google like gcp tells you like pick up and go in 30 seconds effectively so because of that up to 5% of our runs uh failed because of these uh shutdowns um and 5% is a a noticeable especially because it doesn't use customers so almost every customer gets the 5% and especially the long running jobs are more exposed uh to these failures so there are like you know there were couple options about how to overcome this one is well do not use support instance which was not a fully an option but which is something we partly did by retrying on standard nodes so if a test fails for the first time uh then in the second try we're scheduling it to a standard Noe so that that customer uh sees less symptoms of uh of that failure and the second option was um well let's run the test in VMS using like firecracker for example so that we're still in kubernetes but use a micro VM which has snapshot and like know restore capabilities however that required nested virtualization to be enabled or the cluster nodes to be bare metals and neither of them are available in GK and quolf is fully o
