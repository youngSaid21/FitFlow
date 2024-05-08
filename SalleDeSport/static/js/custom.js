// Ecouter le clic de l'utilisateur sur le bouton "Voir plus" dans une carte de cours
$('.btn-outline-dark').click(function() {
    var cours_id = $(this).closest('.card').data('cours-id');

    // Envoyer une requête AJAX pour obtenir les détails du cours
    $.ajax({
        url: '/get_cours_details/',
        method: 'GET',
        data: {'cours_id': cours_id},
        success: function(data) {
            // Afficher les détails du cours dans la modal
            $('#addEmployeeModal .modal-title').text(data.nomCours);
            $('#addEmployeeModal .modal-body').html('<p>' + data.description + '</p>');
            // Afficher la modal
            $('#addEmployeeModal').modal('show');
        }
    });
});
