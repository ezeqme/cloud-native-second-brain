---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Serverless"
themes: ["Kubernetes Core", "SRE Reliability"]
speakers: ["Tom Kerkhove", "Codit"]
sched_url: https://kccnceu2021.sched.com/event/iE5l/application-autoscaling-made-easy-with-kubernetes-event-driven-autoscaling-tom-kerkhove-codit
youtube_search_url: https://www.youtube.com/results?search_query=Application+Autoscaling+Made+Easy+With+Kubernetes+Event-Driven+Autoscaling+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Application Autoscaling Made Easy With Kubernetes Event-Driven Autoscaling - Tom Kerkhove, Codit

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Serverless]]
- Temas: [[Kubernetes Core]], [[SRE Reliability]]
- País/cidade: Virtual / Virtual
- Speakers: Tom Kerkhove, Codit
- Schedule: https://kccnceu2021.sched.com/event/iE5l/application-autoscaling-made-easy-with-kubernetes-event-driven-autoscaling-tom-kerkhove-codit
- Busca YouTube: https://www.youtube.com/results?search_query=Application+Autoscaling+Made+Easy+With+Kubernetes+Event-Driven+Autoscaling+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Application Autoscaling Made Easy With Kubernetes Event-Driven Autoscaling.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE5l/application-autoscaling-made-easy-with-kubernetes-event-driven-autoscaling-tom-kerkhove-codit
- YouTube search: https://www.youtube.com/results?search_query=Application+Autoscaling+Made+Easy+With+Kubernetes+Event-Driven+Autoscaling+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H5eZEq_wqSE
- YouTube title: Application Autoscaling Made Easy With Kubernetes Event-Driven Autoscaling - Tom Kerkhove, Codit
- Match score: 0.966
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/application-autoscaling-made-easy-with-kubernetes-event-driven-autosca/H5eZEq_wqSE.txt
- Transcript chars: 22390
- Keywords: basically, scaling, cluster, authentication, trigger, simple, scaled, application, already, secret, external, running, metric, metrics, prometheus, actually, manage, object

### Resumo baseado na transcript

good morning good evening wherever you are welcome to this talk about kubernetes event driven auto scaling where i'll show you how you can do application auto scaling which makes it super simple on kubernetes so first before we dive into it so my name is tom carkova uh i'm an azure architect at a company called called it and i am one of the co-maintainers of cada and if you want to reach out to me you can always find me on github or you can also pick me

### Excerpt da transcript

good morning good evening wherever you are welcome to this talk about kubernetes event driven auto scaling where i'll show you how you can do application auto scaling which makes it super simple on kubernetes so first before we dive into it so my name is tom carkova uh i'm an azure architect at a company called called it and i am one of the co-maintainers of cada and if you want to reach out to me you can always find me on github or you can also pick me on twitter we are always open for feedback so don't hesitate to reach out so before we get started let's have a look at how you can auto scale applications on kubernetes without cana so plain old kubernetes fresh cluster how would that work so if you have a look imagine we have four deployments which represents applications what you would typically do is you use a horizontal part autoscaler which allows you to scale on cpu and memory so this works fine in vanilla kubernetes now imagine you want to scale on one or more of these external dependencies at the top of the slide how would that look like so over over on the kubernetes side you would use what's called an external metric which basically defines these metrics from outside of the cluster now before you can use these external metrics you would need to use a metric adapter so a metric adapter basically pulls the metric from one of those systems makes them available for you to automatically scale on now there is a caveat however you can only use one metric adapter so if you want to use multiple of these systems you'll have to choose one and make sure all the metrics are available in that one too so in this case imagine you want to auto scale on prometheus kafka and azure monitor what you could do is then send all metrics from kafka to prometheus send all metrics from azure monitor to prometheus by using a tool like prometer now all of this is a bit much and we with gada figured we can make this a lot simpler so that you don't have to worry about all of this auto scaling infrastructure so with cada we basically have a variety of scalars and secret sources so that you can automatically scale deployments jobs or practically anything inside your cluster that has a slash scale super resource so it could be also a resource from a crv from another tool that you're using then you just choose one of the 30 or more built-in scalers that we have or you can build your own or you can use an external scale from the community and you scale your application by using that
