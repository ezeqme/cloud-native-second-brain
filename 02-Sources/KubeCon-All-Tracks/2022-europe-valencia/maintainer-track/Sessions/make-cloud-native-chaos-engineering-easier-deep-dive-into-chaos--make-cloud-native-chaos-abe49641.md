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
speakers: ["Cwen Yin", "PingCAP"]
sched_url: https://kccnceu2022.sched.com/event/ytu4/make-cloud-native-chaos-engineering-easier-deep-dive-into-chaos-mesh-cwen-yin-pingcap
youtube_search_url: https://www.youtube.com/results?search_query=Make+Cloud+Native+Chaos+Engineering+Easier+-+Deep+Dive+into+Chaos+Mesh+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Make Cloud Native Chaos Engineering Easier - Deep Dive into Chaos Mesh - Cwen Yin, PingCAP

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Spain / Valencia
- Speakers: Cwen Yin, PingCAP
- Schedule: https://kccnceu2022.sched.com/event/ytu4/make-cloud-native-chaos-engineering-easier-deep-dive-into-chaos-mesh-cwen-yin-pingcap
- Busca YouTube: https://www.youtube.com/results?search_query=Make+Cloud+Native+Chaos+Engineering+Easier+-+Deep+Dive+into+Chaos+Mesh+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Make Cloud Native Chaos Engineering Easier - Deep Dive into Chaos Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytu4/make-cloud-native-chaos-engineering-easier-deep-dive-into-chaos-mesh-cwen-yin-pingcap
- YouTube search: https://www.youtube.com/results?search_query=Make+Cloud+Native+Chaos+Engineering+Easier+-+Deep+Dive+into+Chaos+Mesh+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bZnI5omUKe4
- YouTube title: Make Cloud Native Chaos Engineering Easier - Deep Dive into Chaos Mesh - Cwen Yin, PingCAP
- Match score: 0.969
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/make-cloud-native-chaos-engineering-easier-deep-dive-into-chaos-mesh/bZnI5omUKe4.txt
- Transcript chars: 24309
- Keywords: network, experiments, application, define, workflow, dashboard, command, schedule, moment, simple, selector, object, create, install, control, components, target, tutorials

### Resumo baseado na transcript

hello everyone and welcome to cook calm and i am very happy to have this opportunity to talk here today my topic is math class clock house engineering ether dev deep into classmates before my sharing i will introduce myself my name is steven you also can call me chungwen is okay i am a maintainer and founder of the chaosman project and present i am working at pincap and also my chaos engineering and the cosmetic journey also study and this company maybe some people are not familiar with

### Excerpt da transcript

hello everyone and welcome to cook calm and i am very happy to have this opportunity to talk here today my topic is math class clock house engineering ether dev deep into classmates before my sharing i will introduce myself my name is steven you also can call me chungwen is okay i am a maintainer and founder of the chaosman project and present i am working at pincap and also my chaos engineering and the cosmetic journey also study and this company maybe some people are not familiar with this company pincap is an open source infrastructure company that has open source many well-known and request tools such as pidp and distributed this and also include the cncf graduated projects tftv and also include cosmetics and so on and present i'm working on this pincap and this company as a tech leader of the chelsea engineering team and also practice accounts and nearly on tidb and trdb cloud to improve their stability and so on um and next as uh most of people know and fast i t series uh service has become more and more complex because they maybe use the difference distribute systems and they may be used on cloud native architecture and so on and cognitive architectures improve their scalability scalable scalables and the flexibility of the applications and but they also involves many challenges such as and then maybe have a more unstable network requires and they can be maybe have more disk failures and they have more um power power failures and so on and all kind of the failures um failures can fall force can happen anytime anywhere else and in any way so many phones can't be avoided we can avoid many force such as the unstable network and the disk failures and so on so and just the writing test and the debugging for this issue is very hard when we developed a distributed with tidb we also have the same issues and we want to find a solution to improve the distributed base stabilities so finally we find kelsey and urine and here is our official or official definitions of the chaos and diaries it says chelsea nearing is about breaking sins in control in control and stacking environment and the source of well-planned experiments in order to build conditions in your application to withstand turbulent conditions and by these definitions the key word is experiments this requires users when they do case improvements they can work hard to figure out the cause of the problems and to find the potential of the problems that you stress them rather than just conducting a simpl
