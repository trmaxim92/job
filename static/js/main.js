
document.addEventListener('alpine:init', () => {
    
    Alpine.store('filters', {
        jobType: '',
        schedule: '',
        paymentType: '',
        salaryMin: '',
        category: '',
        
        applyFilters() {
            const params = new URLSearchParams();
            if (this.jobType) params.append('job_type', this.jobType);
            if (this.schedule) params.append('schedule', this.schedule);
            if (this.paymentType) params.append('payment_type', this.paymentType);
            if (this.salaryMin) params.append('salary_min', this.salaryMin);
            if (this.category) params.append('category', this.category);
            
            window.location.search = params.toString();
        },
        
        clearFilters() {
            this.jobType = '';
            this.schedule = '';
            this.paymentType = '';
            this.salaryMin = '';
            this.category = '';
            window.location.search = '';
        }
    });
    
   
    Alpine.data('mobileMenu', () => ({
        open: false,
        toggle() {
            this.open = !this.open;
        }
    }));
});


$(document).ready(function() {
    
    $('[data-toggle="tooltip"]').tooltip();
    
   
    $('.quick-apply').click(function(e) {
        e.preventDefault();
        const jobId = $(this).data('job-id');
        
        $.ajax({
            url: `/jobs/${jobId}/apply/`,
            method: 'POST',
            data: {
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val(),
                quick_apply: true
            },
            success: function(response) {
                alert('Ваша заявка успешно отправлена!');
                $(`.quick-apply[data-job-id="${jobId}"]`).replaceWith(
                    '<span class="text-green-600">Заявка отправлена</span>'
                );
            },
            error: function(xhr) {
                if (xhr.status === 403) {
                    window.location.href = '/accounts/login/?next=' + window.location.pathname;
                } else {
                    alert('Произошла ошибка при отправке заявки.');
                }
            }
        });
    });
    
    
    if ($('#location-input').length) {
        $('#location-input').autocomplete({
            source: function(request, response) {

                $.getJSON('https://geocode-maps.yandex.ru/1.x/', {
                    format: 'json',
                    geocode: request.term,
                    apikey: 'YOUR_YANDEX_MAPS_API_KEY'
                }, function(data) {
                    response($.map(data.response.GeoObjectCollection.featureMember, function(item) {
                        return {
                            label: item.GeoObject.name + ', ' + item.GeoObject.description,
                            value: item.GeoObject.name,
                            point: item.GeoObject.Point.pos
                        };
                    }));
                });
            },
            select: function(event, ui) {
                const coords = ui.item.point.split(' ');
                $('#id_longitude').val(coords[0]);
                $('#id_latitude').val(coords[1]);
            }
        });
    }
});