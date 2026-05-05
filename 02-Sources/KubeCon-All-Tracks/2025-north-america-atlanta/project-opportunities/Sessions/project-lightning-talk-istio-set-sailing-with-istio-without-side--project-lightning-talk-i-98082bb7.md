---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Project Opportunities"
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Lin Sun", "Maintainer and Lead"]
sched_url: https://kccncna2025.sched.com/event/27d4r/project-lightning-talk-istio-set-sailing-with-istio-without-sidecars-lin-sun-maintainer-and-lead
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Istio%3A+Set+Sailing+With+Istio+Without+Sidecars+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Istio: Set Sailing With Istio Without Sidecars - Lin Sun, Maintainer and Lead

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Atlanta
- Speakers: Lin Sun, Maintainer and Lead
- Schedule: https://kccncna2025.sched.com/event/27d4r/project-lightning-talk-istio-set-sailing-with-istio-without-sidecars-lin-sun-maintainer-and-lead
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Istio%3A+Set+Sailing+With+Istio+Without+Sidecars+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Istio: Set Sailing With Istio Without Sidecars.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27d4r/project-lightning-talk-istio-set-sailing-with-istio-without-sidecars-lin-sun-maintainer-and-lead
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Istio%3A+Set+Sailing+With+Istio+Without+Sidecars+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=SwB7W8g9r6I
- YouTube title: Project Lightning Talk: Istio: Set Sailing With Istio Without Sidecars - Lin Sun
- Match score: 1.024
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-istio-set-sailing-with-istio-without-sidecars/SwB7W8g9r6I.txt
- Transcript chars: 4935
- Keywords: version, ambient, traffic, application, simple, routes, waypoint, without, deployed, control, running, nameace, policy, already, handle, change, istio, actually

### Resumo baseado na transcript

So, I'm actually going to keep it simple because this is my only slides. And in the nameace of default um so uh we're going to look at the labels on the namespace to enroll a pod into ambient. The first routes is from the isial ingress gateway to the demo application. You can see uh it just simply uh when the traffic arrives on port 80, it allows uh routes to the demo application. So what I'm going to do is go in there and you can see this is my demo application and this connects to the rack service. uh traditional psychic but with simple lighter architecture remove the lead of psychob that's exactly what ambient is by the way the reason I'm using rag is I could chat uh with a llama and lava model and if I ask what is still ambient

### Excerpt da transcript

All right. Uh, good afternoon. How's everybody doing? Yes. All right. How many of you heard of Isto? Raise your hand. All right. How many of you heard is still ambient? Okay. A few of you. Well, a third of you. All right. So, I'm actually going to keep it simple because this is my only slides. Uh, we're going to talk about STO ambient. uh basically running service mesh without sidecar. So without further ado, this is odd to do a demo. So let me adjust this a little bit. Um I'm going to show you uh quickly how is your ambient works. This is my Kubernetic cluster. In my default name space, I have my demo application deployed. I also have uh rags uh pods deployed. You can see version one and version two I have it deployed. Uh notice I'm not running any sidecar. I'm doing one slash one, right? So that means my pod only has one container. And in the nameace of default um so uh we're going to look at the labels on the namespace to enroll a pod into ambient. There's no need to restart your application pod. All you need to do is add this magical label is still.iodat mode.

By the way, can you guys see uh is the font size okay for the folks in the back? Good. Thanks. All you need to do is mark a data plane mode equals ambient. So that enrolls all the paths in this particular namespace into ambient because I'm also going to do use some of the layer 7 policy enforcement which I'm going to use HTTP routes to control traffic shifting between my uh rag version one and version two. So I also use a waypoint in my nameace and not only I have the waypoints deployed which I will show you uh after I get out of this panel um I also mark the name space to say I want to use that waypoint deploy in my nameace. This is important so that you could potentially deploy a waypoint and not using it and just test it. So you can see uh this is my waypoint and I already have my name space just by two simple label. I enroll all the pods into ambient and I also said all the pods um I want to use this particular waypoint on the HTTP routes. Um I have two simple routes. The first routes is from the isial ingress gateway to the demo application.

You can see uh it just simply uh when the traffic arrives on port 80, it allows uh routes to the demo application. And I also have a simple rag route which allows me to control traffic to the rag version one and version two. Right now it's very simple. I route all the traffic to version one. So with that I'm going to show you the demo application. Um I
