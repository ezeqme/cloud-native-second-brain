---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "Application + Development"
themes: ["SRE Reliability"]
speakers: ["Matthew LeRay", "Speedscale", "Omid Azizi", "New Relic"]
sched_url: https://kccnceu2022.sched.com/event/ytpE/reproducing-production-issues-in-your-ci-pipeline-using-ebpf-matthew-leray-speedscale-omid-azizi-new-relic
youtube_search_url: https://www.youtube.com/results?search_query=Reproducing+Production+Issues+in+your+CI+Pipeline+Using+eBPF+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Reproducing Production Issues in your CI Pipeline Using eBPF - Matthew LeRay, Speedscale & Omid Azizi, New Relic

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[Application + Development]]
- Temas: [[SRE Reliability]]
- País/cidade: Spain / Valencia
- Speakers: Matthew LeRay, Speedscale, Omid Azizi, New Relic
- Schedule: https://kccnceu2022.sched.com/event/ytpE/reproducing-production-issues-in-your-ci-pipeline-using-ebpf-matthew-leray-speedscale-omid-azizi-new-relic
- Busca YouTube: https://www.youtube.com/results?search_query=Reproducing+Production+Issues+in+your+CI+Pipeline+Using+eBPF+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Reproducing Production Issues in your CI Pipeline Using eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytpE/reproducing-production-issues-in-your-ci-pipeline-using-ebpf-matthew-leray-speedscale-omid-azizi-new-relic
- YouTube search: https://www.youtube.com/results?search_query=Reproducing+Production+Issues+in+your+CI+Pipeline+Using+eBPF+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_RQLY4KXXG8
- YouTube title: Reproducing Production Issues in your CI Pipeline Using eBPF - Matthew LeRay & Omid Azizi
- Match score: 0.908
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/reproducing-production-issues-in-your-ci-pipeline-using-ebpf/_RQLY4KXXG8.txt
- Transcript chars: 29303
- Keywords: traffic, ebpf, information, production, application, little, cluster, change, pipeline, kernel, anything, replay, actually, probably, itself, scripts, github, trace

### Resumo baseado na transcript

all right welcome everyone uh we're really happy to be here today to talk about reproducing production issues in your ci pipeline using ebpf um so yeah um my name is omid um i work at new relic i'm a engineer there principal engineer um i was a founding engineer at pixie so i've spent quite a bit of time working on observability getting data with ebpf and we're going to talk a lot more about that in the talk and i'm super excited to be here matt hey so

### Excerpt da transcript

all right welcome everyone uh we're really happy to be here today to talk about reproducing production issues in your ci pipeline using ebpf um so yeah um my name is omid um i work at new relic i'm a engineer there principal engineer um i was a founding engineer at pixie so i've spent quite a bit of time working on observability getting data with ebpf and we're going to talk a lot more about that in the talk and i'm super excited to be here matt hey so my name is matt larae i work at a startup called speed scale and i hate writing tests so that's what our talk's going to be about is how you can get good testing without uh without writing tests which is also what my company speed skill focuses on thanks for the applause yeah we did better all right okay so like i said i i hate writing tests um and probably you do too one of the things we did in previous generations of technology is we would go and write these handcrafted tests where we would go and make sure it's going to work we would try to guess problem is is we still have huge numbers of production incidents so what i kind of was trying to accomplish with this talk is give everybody a bunch of easy things you can do right github repositories you can go look at that will show you how to in how to instrument your application and run realistic test scenarios uh using traffic replay in your continuous integration pipeline so um that is uh that's that's what we're trying to achieve is get more tests better tests with automation not with human intervention so what is traffic replay now you may have heard of this before it's been around the industry a little bit but basically when it comes to software quality and validation it means treating your tests like uh cattle not pets so instead of having those hand curated hand curated tests much like your kubernetes infrastructure you also you want to have them continuously refreshed you want to just blow them away get rid of all the tests when they're not not valid anymore and you want to treat it as a system that's continuously updating instead of as this this sort of written and you know cast in concrete sort of thing so a couple different approaches to software quality that every well many people probably are using if you're an early adopter of kubernetes and cloud native you probably have tried to test and prod which i like to live dangerously too uh that's great i do a lot of testing in prod sometimes by accident and uh but there are some limitations to doing t
