---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Operations + Performance"
themes: ["AI ML", "SRE Reliability"]
speakers: ["Nick Rutigliano", "Andrew Halaney", "Netflix"]
sched_url: https://kccnceu2026.sched.com/event/2CW7o/is-the-agent-in-the-room-with-us-right-now-nick-rutigliano-andrew-halaney-netflix
youtube_search_url: https://www.youtube.com/results?search_query=Is+the+Agent+in+the+Room+with+Us+Right+Now%3F+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Is the Agent in the Room with Us Right Now? - Nick Rutigliano & Andrew Halaney, Netflix

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Operations + Performance]]
- Temas: [[AI ML]], [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Nick Rutigliano, Andrew Halaney, Netflix
- Schedule: https://kccnceu2026.sched.com/event/2CW7o/is-the-agent-in-the-room-with-us-right-now-nick-rutigliano-andrew-halaney-netflix
- Busca YouTube: https://www.youtube.com/results?search_query=Is+the+Agent+in+the+Room+with+Us+Right+Now%3F+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Is the Agent in the Room with Us Right Now?.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7o/is-the-agent-in-the-room-with-us-right-now-nick-rutigliano-andrew-halaney-netflix
- YouTube search: https://www.youtube.com/results?search_query=Is+the+Agent+in+the+Room+with+Us+Right+Now%3F+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-rwTJebNC10
- YouTube title: Is the Agent in the Room with Us Right Now? - Nick Rutigliano & Andrew Halaney, Netflix
- Match score: 0.763
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/is-the-agent-in-the-room-with-us-right-now/-rwTJebNC10.txt
- Transcript chars: 34884
- Keywords: container, actually, containerd, running, notify, create, namespace, resource, limits, isolation, containers, systemd, mounts, spaces, runtime, cublet, workload, network

### Resumo baseado na transcript

Um, we work on the compute runtime team, which is responsible for our Kubernetes or Titus data plane and the base OS for Netflix. We're going to talk how our container workloads aren't really standard Kubernetes workloads. I'd say probably the majority um they can bring their own storage mediums and we attach those in kind of non-standard ways due to the history of um our platform and then we have I think pretty good resource isolation between nodes. Um some of these are configurable either via your podspec that you actually give to the Kubernetes API or they're configured via how you set up your containerd or your cublet. So how Kubernetes does this is you just set pod.spec.host users to false and uh it kind of goes from there. Um, so Kubernetes, you know, all these pods should be isolated with with respect to anything user related with username spaces enabled.

### Excerpt da transcript

Thanks for coming to our talk. Last one for the conference here. So, I appreciate you hanging around. Um, is the agent in the room with us right now. You look like humans, so I think we're good to go. Um, I'm Andrew Heleni. I'm a senior software engineer here at Netflix. I'm Nicotiano. I'm a senior SR here at Netflix. Um, we work on the compute runtime team, which is responsible for our Kubernetes or Titus data plane and the base OS for Netflix. Uh so what are we going to talk about today? Um we're going to explain briefly what Titus is. It's our container platform internally. We're going to talk how our container workloads aren't really standard Kubernetes workloads. They're not Kubernetes aware at all. Um and that has some kind of weird expectations. Um but we do use Kubernetes under the hood. And so we want to talk about things we do on the data plane on the host to isolate um pods from other pods. So you know things like noisy neighbor problems or if a container was to escape isolation how we could limit the blast radius from that context.

Uh so first what is Titus? It's basically a simple API um internally that we use. So you would say like here's my container image. I want this much resource um like you know four CPUs let's say um and under the hood we make it happen. Um it's got a really long history. Um started out on msos. Uh then we kind of shifted to like a super thin podspec using virtual cublet and docker. We eventually kind of flushed out this podspec more and more and found that you know using virtual cublet and docker on our own data plane was quite limiting. Uh so the last year we have migrated to using cublet and containerd with a bunch of plugins um to kind of keep the expectations we had prior in the same isolation. Um, so our workloads uh really kind of look like a VM to our users. Uh, that's the world they came from originally and they still expect that kind of behavior. Um, so we do weird things like we inject SSH among other processes into the containers pit namespace directly. Um, we let them think they're running as root at least.

Um, we run systemd in a lot of these containers. I'd say probably the majority um they can bring their own storage mediums and we attach those in kind of non-standard ways due to the history of um our platform and then we have I think pretty good resource isolation between nodes. We run some latency sensitive applications and it's a multi-tenant environment and typically we don't have a whole lot of is
