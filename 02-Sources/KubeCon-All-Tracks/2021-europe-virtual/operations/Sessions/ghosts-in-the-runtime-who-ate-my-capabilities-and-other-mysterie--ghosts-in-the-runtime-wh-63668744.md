---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Operations"
themes: ["AI ML", "Storage Data", "Runtime Containers"]
speakers: ["Laurent Bernaille", "Eric Mountain", "Datadog"]
sched_url: https://kccnceu2021.sched.com/event/iE22/ghosts-in-the-runtime-who-ate-my-capabilities-and-other-mysteries-laurent-bernaille-eric-mountain-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Ghosts+in+the+Runtime%3A+Who+Ate+My+Capabilities+and+Other+Mysteries+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Ghosts in the Runtime: Who Ate My Capabilities and Other Mysteries - Laurent Bernaille & Eric Mountain, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Operations]]
- Temas: [[AI ML]], [[Storage Data]], [[Runtime Containers]]
- País/cidade: Virtual / Virtual
- Speakers: Laurent Bernaille, Eric Mountain, Datadog
- Schedule: https://kccnceu2021.sched.com/event/iE22/ghosts-in-the-runtime-who-ate-my-capabilities-and-other-mysteries-laurent-bernaille-eric-mountain-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Ghosts+in+the+Runtime%3A+Who+Ate+My+Capabilities+and+Other+Mysteries+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Ghosts in the Runtime: Who Ate My Capabilities and Other Mysteries.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE22/ghosts-in-the-runtime-who-ate-my-capabilities-and-other-mysteries-laurent-bernaille-eric-mountain-datadog
- YouTube search: https://www.youtube.com/results?search_query=Ghosts+in+the+Runtime%3A+Who+Ate+My+Capabilities+and+Other+Mysteries+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1bi5H9hMuFY
- YouTube title: Ghosts in the Runtime: Who Ate My Capabilities & Other Mysteries- Laurent Bernaille & Eric Mountain,
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/ghosts-in-the-runtime-who-ate-my-capabilities-and-other-mysteries/1bi5H9hMuFY.txt
- Transcript chars: 25066
- Keywords: container, actually, capabilities, network, runtime, cubelet, namespace, happening, process, looked, address, function, running, everything, allowed, message, plugin, kernel

### Resumo baseado na transcript

hello uh we're very happy to be there with you today uh we'd rather be live with you and hopefully we might be able to uh in los angeles right uh so we are lujan eric and we're going to share stories about low-level problems uh we face from kubernetes we showed a few stories in the past about control plane challenges but today we're going to focus on what happens on nodes so in case you don't know datadog uh we're a monitoring company but today we're not going will challenge you to go deep in your understanding of the of kubernetes and the overall ecosystem but it is extremely interesting to do so we have maybe a strange definition of fun but we definitely like digging into these kinds of issues we think

### Excerpt da transcript

hello uh we're very happy to be there with you today uh we'd rather be live with you and hopefully we might be able to uh in los angeles right uh so we are lujan eric and we're going to share stories about low-level problems uh we face from kubernetes we showed a few stories in the past about control plane challenges but today we're going to focus on what happens on nodes so in case you don't know datadog uh we're a monitoring company but today we're not going to talk about the product we're going to talk about the infrastructure behind the products and uh it's pretty large uh we're running tens of thousands of hosts and dozens of clusters uh with up to four thousand nodes uh and it comes with uh multiple challenges and this is what we're going to talk about today so we have a few stories uh not completely related but they they all happen locally on notes and we're going to to focus on that so let's start uh with this first story about disappearing containers so it started uh with this simple graph here when we migrated an application from a virtual machine to kubernetes and we noticed that the cpu profile was very different which was a bit worrying right so we looked at uh the pods running this application and we discovered that several of them were in great container error actually about 10 of them so they were not ready and not processing traffic we found very easy solutions to address this by editing the bird or researching the cubelet but it wasn't very satisfying so the first thing we did was try to understand what this error was so we looked at the qubit logs and basically the qubit is getting an error for the runtime containing in our case uh because it's trying it seems to be trying to create a container that already exists according to the runtime and it's doing this a lot as you can see here with 62 attempts right and it keeps retrying and getting the exact same results so of course we wonder well who is right uh who is wrong so the cubit believes it needs to create a container what about continuity so if we have container d this container is actually running completely fine the next step was to try and reproduce a problem in a test environment and we had noticed that it seemed to be related with cubelet restarts so we did a very simple script that we started the cubelet frequently and after only an hour as you can see all the parts in the deployment were in the same era so we were able to very easily reproduce it right so what is this error exa
